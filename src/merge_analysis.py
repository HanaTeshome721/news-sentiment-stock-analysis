import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def merge_sentiment_and_price(sentiment_df, price_df, stock_ticker):
    merged = pd.merge(sentiment_df[sentiment_df['stock'] == stock_ticker],
                      price_df, on='date', how='inner')
    return merged

def plot_correlation(merged_df, stock_ticker):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='avg_sentiment', y='daily_return', data=merged_df)
    sns.regplot(x='avg_sentiment', y='daily_return', data=merged_df, scatter=False, color='red')
    plt.title(f'Correlation between Sentiment and Daily Return: {stock_ticker}')
    plt.xlabel('Average Sentiment')
    plt.ylabel('Daily Return')
    plt.show()
    
    corr = merged_df['avg_sentiment'].corr(merged_df['daily_return'])
    print(f'Correlation coefficient for {stock_ticker}: {corr:.4f}')

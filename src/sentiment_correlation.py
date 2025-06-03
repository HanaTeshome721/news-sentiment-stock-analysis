import pandas as pd
from textblob import TextBlob
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Define paths
STOCK_FILES = {
    "AAPL": "data/yfinance_data/AAPL_historical_data.csv",
    "AMZN": "data/yfinance_data/AMZN_historical_data.csv",
    "GOOG": "data/yfinance_data/GOOG_historical_data.csv",
    "META": "data/yfinance_data/META_historical_data.csv",
    "MSFT": "data/yfinance_data/MSFT_historical_data.csv",
    "NVDA": "data/yfinance_data/NVDA_historical_data.csv",
    "TSLA": "data/yfinance_data/TSLA_historical_data.csv",
}

NEWS_PATH = "data/raw_analyst_ratings.csv"  # Adjust if named differently

# 1. Load and prepare news data
def load_and_prepare_news():
    df_news = pd.read_csv(NEWS_PATH)
    df_news['date'] = pd.to_datetime(df_news['date']).dt.date
    df_news['sentiment'] = df_news['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    daily_sentiment = df_news.groupby(['date', 'stock'])['sentiment'].mean().reset_index()
    return daily_sentiment

# 2. Load and prepare stock data
def load_stock_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df['Date'] = df['Date'].dt.date
    df['daily_return'] = df['Close'].pct_change()
    return df[['Date', 'daily_return']].dropna()

# 3. Merge news and stock data, compute correlation
def analyze_correlation(stock_symbol, news_sentiment_df):
    stock_df = load_stock_data(STOCK_FILES[stock_symbol])
    sentiment_df = news_sentiment_df[news_sentiment_df['stock'] == stock_symbol]
    merged = pd.merge(stock_df, sentiment_df, left_on='Date', right_on='date')
    
    if merged.empty:
        print(f"No overlapping dates for {stock_symbol}")
        return None
    
    corr, _ = pearsonr(merged['daily_return'], merged['sentiment'])
    print(f"{stock_symbol} Correlation: {corr:.3f}")
    
    # Plot
    sns.scatterplot(x='sentiment', y='daily_return', data=merged)
    plt.title(f'{stock_symbol} - Sentiment vs. Daily Return')
    plt.xlabel('Average Daily Sentiment')
    plt.ylabel('Daily Return (%)')
    plt.grid(True)
    plt.show()
    
    return corr

# Run all
if __name__ == "__main__":
    news_sentiment_df = load_and_prepare_news()
    correlations = {}

    for stock in STOCK_FILES:
        corr = analyze_correlation(stock, news_sentiment_df)
        if corr is not None:
            correlations[stock] = corr

    print("All Correlations:")
    for stock, corr in correlations.items():
        print(f"{stock}: {corr:.3f}")

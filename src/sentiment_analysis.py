import pandas as pd
from textblob import TextBlob

def compute_sentiment_score(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def add_sentiment_scores(news_df):
    news_df['sentiment_score'] = news_df['headline'].apply(compute_sentiment_score)
    return news_df

def aggregate_daily_sentiment(news_df):
    daily_sentiment = (
        news_df.groupby(['date', 'stock'])['sentiment_score']
        .mean()
        .reset_index()
        .rename(columns={'sentiment_score': 'avg_sentiment'})
    )
    return daily_sentiment

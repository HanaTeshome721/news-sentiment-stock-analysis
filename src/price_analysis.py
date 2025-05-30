import pandas as pd

def calculate_daily_return(price_df):
    price_df['Date'] = pd.to_datetime(price_df['Date'])
    price_df['daily_return'] = (price_df['Close'] - price_df['Open']) / price_df['Open']
    daily_returns = price_df[['Date', 'daily_return']]
    return daily_returns.rename(columns={'Date': 'date'})

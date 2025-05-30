import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.feature_extraction.text import CountVectorizer

def headline_length_stats(df):
    df['headline_length'] = df['headline'].apply(len)
    print(df['headline_length'].describe())
    sns.histplot(df['headline_length'], bins=20, kde=True)
    plt.title('Headline Length Distribution')
    plt.show()

def articles_per_publisher(df):
    publisher_counts = df['publisher'].value_counts()
    print(publisher_counts)
    publisher_counts.plot(kind='bar')
    plt.title('Articles per Publisher')
    plt.ylabel('Count')
    plt.show()

def publication_date_trends(df):
    df['date_only'] = pd.to_datetime(df['date']).dt.date
    daily_counts = df.groupby('date_only').size()
    daily_counts.plot(figsize=(12, 6))
    plt.title('Articles Published Over Time')
    plt.ylabel('Number of Articles')
    plt.show()



def publication_hour_analysis(df):
    df['hour'] = pd.to_datetime(df['date']).dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()
    hourly_counts.plot(kind='bar')
    plt.title('Articles Published by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Articles')
    plt.show()



def publisher_domain_analysis(df):
    if df['publisher'].str.contains('@').any():
        df['domain'] = df['publisher'].str.extract(r'@([\w\.-]+)')
        domain_counts = df['domain'].value_counts()
        print(domain_counts)
        domain_counts.plot(kind='bar')
        plt.title('Top Publisher Domains')
        plt.show()
    else:
        print("No email-format publishers found.")



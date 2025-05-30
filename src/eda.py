import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.feature_extraction.text import CountVectorizer

# Descriptive Statistics
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
    # Mixed format parsing
    df['datetime_parsed'] = pd.to_datetime(df['date'], format='mixed', errors='coerce', utc=True)

    # Drop rows with bad dates
    df_clean = df.dropna(subset=['datetime_parsed'])

    # Extract just the date part
    df_clean['date_only'] = df_clean['datetime_parsed'].dt.date

    # Group and plot
    daily_counts = df_clean.groupby('date_only').size()
    daily_counts.plot(figsize=(12, 6), title='Articles per Day')
    plt.ylabel('Number of Articles')
    plt.show()



#  Text Analysis (Topic Modeling)
def top_keywords(df, num_keywords=20):
    vectorizer = CountVectorizer(stop_words='english', max_features=num_keywords)
    X = vectorizer.fit_transform(df['headline'])
    keywords = vectorizer.get_feature_names_out()
    counts = X.toarray().sum(axis=0)
    keyword_freq = pd.Series(counts, index=keywords).sort_values(ascending=False)
    print(keyword_freq)
    keyword_freq.plot(kind='bar')
    plt.title(f'Top {num_keywords} Keywords in Headlines')
    plt.show()



# Time Series Analysis
def publication_hour_analysis(df):
    df['datetime_parsed'] = pd.to_datetime(df['date'], utc=True, errors='coerce')
    df_clean = df.dropna(subset=['datetime_parsed'])

    df_clean['hour'] = df_clean['datetime_parsed'].dt.hour

    hourly_counts = df_clean['hour'].value_counts().sort_index()
    hourly_counts.plot(kind='bar')
    plt.title('Articles Published by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Articles')
    plt.show()



#  Publisher Domain Analysis
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




# 📝 Script: EDA for News-Sentiment-Stock-Analysis

This script (`eda.py`) performs **exploratory data analysis (EDA)** on a dataset of news headlines related to stock movements.

It helps you understand:
✅ How long the headlines are  
✅ Which publishers are most active  
✅ Daily publishing trends  
✅ Most common keywords  
✅ When (by hour) articles are published

---

## 📂 Input

The script expects a **CSV file** with at least these columns:
- `headline` → the news headline text  
- `url` → (optional) link to the article  
- `publisher` → the name of the publishing source  
- `date` → publication datetime (ISO format, e.g., `2020-06-05 10:30:54-04:00`)  
- `stock` → the stock symbol (e.g., AAPL, MSFT)

Make sure the CSV is loaded into a pandas DataFrame (`df`) before passing it to the script’s functions.

---

## ⚙️ What Does It Do?

The script contains these main functions:

### 1️⃣ `headline_length_stats(df)`
- Calculates headline length stats (min, max, mean, etc.)
- Plots a histogram of headline lengths

### 2️⃣ `articles_per_publisher(df)`
- Counts articles per publisher
- Plots a bar chart showing which publishers are most active

### 3️⃣ `publication_date_trends(df)`
- Extracts daily article counts
- Plots article publishing trends over time

### 4️⃣ `top_keywords(df, num_keywords=20)`
- Uses `CountVectorizer` to find top N keywords (default 20)
- Plots a bar chart of the most frequent words

### 5️⃣ `publication_hour_analysis(df)`
- Extracts the hour of the day articles were published
- Plots a bar chart showing publication patterns by hour

---

## ▶️ How to Run

### Script usage
```bash
python src/eda.py

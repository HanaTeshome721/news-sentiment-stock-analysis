
---

## 📋 Notebook Descriptions

### 🔍 01_data_exploration.ipynb
- Load raw news headline data and stock data
- Perform initial EDA (summary stats, distributions, missing values)
- Visualize publishing trends, sources, and headline patterns

---

### 🛠 02_text_preprocessing.ipynb
- Clean and preprocess headline text
- Remove stopwords, punctuation, apply lowercasing
- Explore word clouds, n-grams, and token frequencies

---

### 💬 03_sentiment_analysis.ipynb
- Apply sentiment scoring (e.g., VADER, TextBlob, or custom models)
- Visualize sentiment distributions across headlines and over time
- Aggregate sentiment scores per stock per day

---

### 📈 04_stock_price_alignment.ipynb
- Align news sentiment with stock price movements
- Join/merge sentiment scores with stock return data
- Visualize correlations and lags between sentiment and price changes

---

### 🤖 05_modeling.ipynb
- Build predictive models (e.g., regression, classification) using sentiment + stock data
- Train/test models, evaluate performance
- Feature importance and error analysis

---

## ⚙️ How to Run

To run these notebooks:

1️⃣ Make sure you have all dependencies installed:
```bash
pip install -r requirements.txt

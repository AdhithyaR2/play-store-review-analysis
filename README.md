# 📱 Play Store Review Sentiment Analysis Dashboard

An interactive AI-powered Streamlit dashboard for analyzing user reviews from the Google Play Store.  
This project uses Natural Language Processing (NLP) techniques to clean, classify, and cluster user reviews based on their sentiment.

---

## 📊 Features

- 📥 Scrape and process real Play Store reviews
- 💬 Perform sentiment analysis using a fine-tuned DistilBERT model
- 🔍 Cluster similar reviews using Sentence-BERT embeddings and KMeans
- 🌥️ Generate dynamic WordClouds for each cluster
- 📈 Visualize sentiment distribution interactively on a clean Streamlit dashboard
- 🚀 Deployed live on [Streamlit Cloud](https://play-store-review-analysis-zrhcy7gxteovzznmyjcxuq.streamlit.app/)

---

## 📦 Tech Stack

- **Python 3.13**
- **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
- **NLTK**, **spaCy**
- **Scikit-learn**
- **Hugging Face Transformers**
- **Sentence-Transformers**
- **Streamlit**
- **WordCloud**

---

## 📁 Project Structure
play-store-review-analysis/
├── data/
│   └── clustered_reviews.csv          # Processed dataset used by the dashboard
├── dashboard.py                       # Streamlit app script
├── scrape_reviews.py                  # (Optional) Scraper for Play Store reviews
├── process_reviews_kaggle.py          # Preprocesses raw reviews from a CSV
├── sentiment_analysis_kaggle.py       # Performs sentiment analysis
├── cluster_reviews_kaggle.py          # Clusters the reviews
├── requirements.txt                   # Project dependencies
└── README.md                          # You’re here!

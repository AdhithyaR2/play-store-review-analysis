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



## 🚀 How to Run Locally

1️⃣ **Clone this repository**
```bash
git clone https://github.com/AdhithyaR2/play-store-review-analysis.git
cd play-store-review-analysis

pip install -r requirements.txt

streamlit run dashboard.py

🌐 Live App

Check out the live app here:
👉 play-store-review-analysis.streamlit.app

📌 Credits
	•	Hugging Face Transformers for pretrained models
	•	Streamlit for rapid deployment
	•	Kaggle Play Store review datasets for testing

📜 License

This project is open-source and available under the MIT License.

📣 Author

Made with ♥️ by Adhithya R


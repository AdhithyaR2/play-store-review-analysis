import pandas as pd
from transformers import pipeline
import torch

# Set device to CPU
device = 0 if torch.cuda.is_available() else -1

# Load cleaned reviews
df = pd.read_csv('data/cleaned_reviews.csv')

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device=device)

# Apply sentiment analysis
def get_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "NEUTRAL"
    result = sentiment_pipeline(text[:512])[0]
    return result['label']

df['sentiment'] = df['clean_content'].apply(get_sentiment)

# Save the sentiment labeled reviews
df.to_csv('data/sentiment_reviews.csv', index=False)

print("✅ Sentiment analysis done and saved to 'data/sentiment_reviews.csv'")

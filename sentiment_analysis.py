import pandas as pd
from transformers import pipeline

# Load cleaned reviews
df = pd.read_csv('data/cleaned_reviews.csv')

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to get sentiment
def get_sentiment(text):
    result = sentiment_pipeline(str(text))[0]
    return result['label']

# Apply sentiment analysis to cleaned_content column
df['sentiment'] = df['clean_content'].apply(get_sentiment)

# Show first 5 results
print(df[['clean_content', 'sentiment']].head())

# Save the result into a new CSV file
df.to_csv('data/sentiment_reviews.csv', index=False)

print("Sentiment analysis done and saved successfully.")

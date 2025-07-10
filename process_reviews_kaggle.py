import pandas as pd
import re

# Load the Kaggle reviews CSV
df = pd.read_csv('data/googleplaystore_user_reviews.csv')  # adjust if your file is differently named

# Drop rows with missing reviews
df = df.dropna(subset=['Translated_Review'])

# Clean the review texts
def clean_text(text):
    text = str(text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove non-letters
    text = text.lower()  # convert to lowercase
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

df['clean_content'] = df['Translated_Review'].apply(clean_text)

# Save the cleaned reviews
df[['clean_content']].to_csv('data/cleaned_reviews.csv', index=False)

print("✅ Reviews cleaned and saved to 'data/cleaned_reviews.csv'")

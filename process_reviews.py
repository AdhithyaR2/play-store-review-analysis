import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the CSV file
df = pd.read_csv('data/app_reviews.csv')

# Function to clean text
def clean_text(text):
    text = str(text).lower()                             # convert to lowercase
    text = re.sub(r'[^a-zA-Z ]', '', text)                # remove punctuation and numbers
    words = text.split()
    words = [word for word in words if word not in stop_words]   # remove stopwords
    return ' '.join(words)

# Apply cleaning to 'content' column
df['clean_content'] = df['content'].apply(clean_text)

# Show first 5 cleaned reviews
print(df[['content', 'clean_content']].head())

# Save cleaned reviews into a new CSV file
df.to_csv('data/cleaned_reviews.csv', index=False)

print("Cleaned reviews saved successfully.")

import pandas as pd

# Load your Kaggle CSV
df = pd.read_csv('data/googleplaystore_user_reviews.csv')  # adjust filename if needed

# Print all column names
print(df.columns)

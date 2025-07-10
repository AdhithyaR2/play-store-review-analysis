import pandas as pd

# Load clustered reviews
df = pd.read_csv('data/clustered_reviews.csv')

# Show number of reviews per cluster
print("Number of reviews per cluster:")
print(df['cluster'].value_counts())
print()

# Show sentiment distribution inside each cluster
print("Sentiment distribution inside each cluster:")
print(df.groupby(['cluster', 'sentiment']).size())

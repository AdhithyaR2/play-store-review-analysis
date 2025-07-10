import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# Load sentiment labeled reviews
df = pd.read_csv('data/sentiment_reviews.csv')

# Drop rows with missing or empty clean_content
df = df.dropna(subset=['clean_content'])
df = df[df['clean_content'].str.strip() != ""]

# Load sentence transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate sentence embeddings for reviews
embeddings = model.encode(df['clean_content'].tolist())

# Perform clustering (let's use 3 clusters for now, adjust if needed)
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(embeddings)

# Add cluster labels to dataframe
df['cluster'] = clusters

# Save the clustered reviews
df.to_csv('data/clustered_reviews.csv', index=False)

print("✅ Clustering completed and saved to 'data/clustered_reviews.csv'")

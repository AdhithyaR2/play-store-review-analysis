import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# Load cleaned reviews
df = pd.read_csv('data/sentiment_reviews.csv')

# Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert clean_content column to list
sentences = df['clean_content'].astype(str).tolist()

# Generate embeddings for each review
embeddings = model.encode(sentences)

# Apply KMeans clustering
num_clusters = 3  # you can adjust this based on how many groupings you want
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(embeddings)

# Add cluster labels to DataFrame
df['cluster'] = kmeans.labels_

# Show first 10 results
print(df[['clean_content', 'sentiment', 'cluster']].head(10))

# Save clustered reviews
df.to_csv('data/clustered_reviews.csv', index=False)

print("Clustering completed and saved successfully.")

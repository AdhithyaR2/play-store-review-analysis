import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Title of the Dashboard
st.title("Google Play Store App Review Analyzer 📱")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a clustered review CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    st.subheader("Number of Reviews per Cluster")
    cluster_counts = df['cluster'].value_counts()
    st.bar_chart(cluster_counts)

    st.subheader("Sentiment Distribution in Clusters")
    sentiment_counts = df.groupby(['cluster', 'sentiment']).size().unstack().fillna(0)
    st.bar_chart(sentiment_counts)

    # Cluster selector
    st.subheader("View Sample Reviews by Cluster")
    selected_cluster = st.selectbox("Select a cluster", sorted(df['cluster'].unique()))

    # Display sample reviews from the selected cluster
    sample_reviews = df[df['cluster'] == selected_cluster][['clean_content', 'sentiment']].sample(5)
    st.write(sample_reviews)

    # Generate and display WordCloud for the selected cluster
    st.subheader("WordCloud for Selected Cluster")

    text = " ".join(df[df['cluster'] == selected_cluster]['clean_content'].astype(str))

    if text.strip() != "":
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.write("No reviews found in this cluster to generate a WordCloud.")

else:
    st.write("⬆️ Upload a clustered review CSV file to get started.")

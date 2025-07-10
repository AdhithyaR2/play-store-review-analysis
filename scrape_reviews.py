from google_play_scraper import reviews
import pandas as pd

# Replace this with your app's package name
package_name = 'com.instagram.android'

# Scrape 200 reviews
result, _ = reviews(
    package_name,
    lang='en',
    country='us',
    count=200
)

# Convert to DataFrame
df = pd.DataFrame(result)

# View the first 5 reviews
print(df[['userName', 'score', 'content']].head())

# Save to CSV file
df.to_csv('data/app_reviews.csv', index=False)

print("Reviews saved successfully.")

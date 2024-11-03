import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Sample dataset with website descriptions and categories
data = {
    'description': [
        'A modern online store with shopping cart functionality and payment integration.',
        'Personal blog with space for articles, comments, and social media links.',
        'Professional portfolio with sections for projects, skills, and contact details.',
        'Corporate website with sections for about us, services, and contact information.',
        'A restaurant website with menu display, reservation system, and contact form.',
        'News site template with category filtering, trending articles, and social media links.',
        'Landing page for product launch with email signup and product showcase.'
    ],
    'template': [
        'e-commerce', 'blog', 'portfolio', 'corporate', 'restaurant', 'news', 'landing page'
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data)
df.to_csv('website_data.csv', index=False)
print("Dataset created successfully!")

# Confirm column names and data
print(df.columns)
print(df.head())

# Plotting the category distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='template')
plt.title('Distribution of Template Categories')
plt.xlabel('Template')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Generating a word cloud for the descriptions
text = " ".join(description for description in df['description'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Descriptions')
plt.show()


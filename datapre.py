from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the dataset
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

# Splitting data into features and target
X = df['description']
y = df['template']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data preprocessed and split successfully!")

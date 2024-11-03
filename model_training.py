import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
import pandas as pd

# Expanded dataset with more examples
data = {
    'description': [
        'A modern online store with shopping cart and secure payment options.',
        'E-commerce website featuring product catalogs, filters, and checkout system.',
        'Online store with a user-friendly interface, categories, and customer reviews.',
        'Blog platform with support for articles, comments, and social media integration.',
        'Personal blog with categories for posts, tags, and a section for reader comments.',
        'Blog with modern design, article archiving, and social sharing options.',
        'Portfolio site to showcase projects, skills, testimonials, and contact form.',
        'Professional portfolio with project galleries, skills overview, and resume upload.',
        'Portfolio with sections for work experience, skills, and downloadable resume.',
        'Corporate website for showcasing company profile, services, and contact details.',
        'Business site with sections for team members, services offered, and case studies.',
        'Corporate page highlighting about us, mission statement, and executive team.',
        'Restaurant website with online menu, reservation system, and location map.',
        'Food service website featuring digital menu, booking options, and contact info.',
        'Restaurant page with menu preview, reservation form, and chef’s specialties.',
        'News website template with categories, trending stories, and sharing options.',
        'News portal with support for categories, breaking news alerts, and live updates.',
        'News site design featuring article categories, trending topics, and comment section.',
        'Landing page for product launch with sign-up form, product showcase, and testimonials.',
        'Product landing page with email capture, product images, and customer testimonials.',
        'One-page product site with call-to-action buttons, media highlights, and FAQs.'
    ],
    'template': [
        'e-commerce', 'e-commerce', 'e-commerce',
        'blog', 'blog', 'blog',
        'portfolio', 'portfolio', 'portfolio',
        'corporate', 'corporate', 'corporate',
        'restaurant', 'restaurant', 'restaurant',
        'news', 'news', 'news',
        'landing page', 'landing page', 'landing page'
    ]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('website_data.csv', index=False)
print("Expanded dataset created successfully!")


# Split the data into features and target
X = df['description']  # Features
y = df['template']     # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# List to store models and their names
models = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": SVC(kernel='linear')
}

# Dictionary to store the model accuracy
results = {}

for model_name, model in models.items():
    # Create a pipeline with TF-IDF and the model
    pipeline = make_pipeline(TfidfVectorizer(), model)
    
    # Train the model
    pipeline.fit(X_train, y_train)
    
    # Make predictions
    y_pred = pipeline.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    results[model_name] = accuracy
    
    # Print classification report
    print(f"Classification Report for {model_name}:\n", classification_report(y_test, y_pred))

# Display results
print("\nModel Accuracies:")
for model_name, accuracy in results.items():
    print(f"{model_name}: {accuracy:.2f}")











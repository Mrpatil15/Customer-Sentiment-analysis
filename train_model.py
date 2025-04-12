import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from utils import preprocess_text

# Sample data
data = {
    "review": [
        "I love this product!",
        "It's okay, not the best",
        "Absolutely terrible. Waste of money",
        "Very satisfied with my purchase",
        "Not great, not terrible",
        "Worst experience ever",
    ],
    "sentiment": ["Positive", "Neutral", "Negative", "Positive", "Neutral", "Negative"]
}

df = pd.DataFrame(data)

# Preprocess
df["cleaned"] = df["review"].apply(preprocess_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned"])
y = df["sentiment"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved.")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


df = pd.read_csv("https://raw.githubusercontent.com/atharva-ingle/Crop-Recommendation-Dataset/master/Crop_recommendation.csv")


X = df.drop('label', axis=1)
y = df['label']


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


joblib.dump(model, "crop_model.pkl")
print(" Model trained and saved as crop_model.pkl")

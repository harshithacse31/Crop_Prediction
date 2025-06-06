# crop_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("cpdata.csv")

# Separate features and target
X = data[['temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a classifier (Random Forest for better results)
model = RandomForestClassifier()
model.fit(X_train_scaled, y_train)

# Test the model
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(acc * 100, 2), "%")

# ----- Crop Prediction -----
# Example input for prediction
input_df = pd.DataFrame([[25.0, 80.0, 6.5, 200.0]], columns=X.columns)
sample_scaled = scaler.transform(input_df)

# Predict the crop
predicted_crop = model.predict(sample_scaled)
print("Predicted Crop:", predicted_crop[0])

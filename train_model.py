import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("heart_data.csv")
X = df[['Age', 'RestBP', 'Cholesterol', 'MaxHR']]
y = df['Target']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("model working")
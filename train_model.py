import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Simple dataset
data = pd.DataFrame({
    'experience': [1, 2, 3, 4, 5],
    'salary': [20000, 30000, 40000, 50000, 60000]
})

X = data[['experience']]
y = data['salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model trained and saved!")
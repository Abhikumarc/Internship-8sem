from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "NEW VERSION RUNNING"

@app.route('/predict')
def predict():
    experience = float(request.args.get('experience'))
    prediction = model.predict([[experience]])

    return {
        'predicted_salary': int(prediction[0])
    }

if __name__ == '__main__':
    app.run(debug=True)
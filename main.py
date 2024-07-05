from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask App of Zameen price predictor!"

@app.route('/predict', methods=['POST'])
def get_data():
    input_data = request.get_json()
    
    size = input_data.get('size', None)
    bedrooms = input_data.get('bedrooms', None)
    bathrooms = input_data.get('bathrooms', None)
    type = input_data.get('type', None)
    
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    prediction = model.predict([[size, bedrooms, bathrooms, type]])
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, )

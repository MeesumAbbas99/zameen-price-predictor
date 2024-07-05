from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

app = FastAPI()

class Item(BaseModel):
    size: int 
    bedrooms: int
    bathrooms: int
    type: int

@app.get('/')
def home():
    return "Welcome to the FastAPI App of Zameen price predictor!"

@app.post('/predict')
def get_data(item: Item):
    size = item.size
    bedrooms = item.bedrooms
    bathrooms = item.bathrooms
    house_type = item.type
    
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    prediction = model.predict([[size, bedrooms, bathrooms, house_type]])
    
    return {'prediction': prediction.tolist()}

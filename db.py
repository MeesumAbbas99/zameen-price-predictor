import pandas as pd
import pymongo

df = pd.read_csv('2100property_data.csv')

data = df.to_dict(index=False, orient = "split")

# Step 1: Create a connection to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')  # Adjust the URI as needed
db = client['mydatabase']  # Replace with your database name
collection = db['mycollection']  # Replace with your collection name

collection.insert_many(data)


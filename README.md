# Zameen Property Price Prediction

## Overview

This project aims to predict property prices in Karachi using machine learning. The data is scraped from Zameen.com, preprocessed, and used to train a linear regression model. The trained model is then exposed through a Flask API for making predictions.

## Project Structure

The project is structured as follows:

- **`data/`**: Contains the scraped data (`zameen_data.csv`) and the preprocessed data used for model training.
- **`model/`**: Holds the trained model (`model.pkl`) and the script (`model.py`) for preprocessing data and training the model.
- **`app/`**: Includes the Flask web application (`app.py`) that serves as the API endpoint for predicting property prices.
- **`templates/`**: Contains the HTML template (`index.html`) for user interface to interact with the API.
- **`static/`**: Includes static files (e.g., CSS, JavaScript) for styling and functionality of the HTML interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/zameen-property-prediction.git
   ```

2. Navigate into the project directory:
   ```bash
   cd zameen-property-prediction
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

1. Place your scraped data CSV (`zameen_data.csv`) in the `data/` directory.

2. Run the model training script:
   ```bash
   python model/model.py
   ```

   This will preprocess the data, train the model, and save it as `model.pkl` in the `model/` directory.

### Running the Flask API

1. Navigate to the `app/` directory:
   ```bash
   cd app
   ```

2. Start the Flask server:
   ```bash
   python app.py
   ```

   The server will start locally at `http://127.0.0.1:5000/`.

### Making Predictions

- Access the API through Thunder Client, Postman, or any API testing tool, using endpoints like `http://127.0.0.1:5000/predict`.

- Alternatively, open `http://127.0.0.1:5000/` in a web browser to use the interactive HTML interface (`index.html`) for making predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML/CSS
- JavaScript

## Author

- Syed Muhammad Meesum Abbas 
- GitHub: [Your GitHub Profile](https://github.com/MeesumAbbas99)


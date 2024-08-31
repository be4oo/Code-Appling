import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import joblib

# Load the model and preprocessors
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('ohe.pkl', 'rb') as file:
    ohe = pickle.load(file)
    
training_data = pd.read_csv('carpricetest.csv')

# Initialize preprocessors
# ohe = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore').set_output(transform='pandas')
# scaler = MinMaxScaler().set_output(transform='pandas')

# Define the numeric and categorical columns in the specified order
numeric_features = ['enginesize', 'curbweight', 'horsepower', 'carwidth', 'highwaympg', 'citympg', 'carlength']
categorical_features = ['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem']

# Fit the preprocessors
# scaler.fit(training_data[numeric_features])
# ohe.fit(training_data[categorical_features])

# When training your model and preprocessors:
# joblib.dump(scaler, 'scaler.joblib')
# joblib.dump(ohe, 'ohe.joblib')

# In your Streamlit app:
# scaler = joblib.load('scaler.joblib')
# ohe = joblib.load('ohe.joblib')

def process_new_data(X_new):
    # Ensure the input DataFrame has columns in the correct order
    X_new = X_new[numeric_features + categorical_features]
    
    X_new_num = scaler.transform(X_new[numeric_features])
    X_new_cat = X_new[categorical_features].astype('object')  # Ensure categorical columns are of type 'object'
    X_new_enc = ohe.transform(X_new_cat)
    X_new_all = pd.concat([X_new_num, X_new_enc], axis=1)
    return X_new_all

# Streamlit app
st.title('Car Price Prediction')

# Input fields for user
st.header('Enter Car Information')

# Numeric inputs
numeric_inputs = {}
for col in numeric_features:
    if col in ['enginesize', 'curbweight', 'horsepower', 'highwaympg', 'citympg']:
        numeric_inputs[col] = st.number_input(f'Enter {col}', min_value=0, step=1, value=0)
    else:
        numeric_inputs[col] = st.number_input(f'Enter {col}', min_value=0.0, format='%.2f')

# Categorical inputs with predefined options
categorical_options = {
    'fueltype': ['gas', 'diesel'],
    'aspiration': ['std', 'turbo'],
    'doornumber': ['two', 'four'],
    'carbody': ['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'],
    'drivewheel': ['rwd', 'fwd', '4wd'],
    'enginelocation': ['front', 'rear'],
    'enginetype': ['ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'],
    'cylindernumber': ['four', 'six', 'five', 'eight', 'two', 'twelve'],
    'fuelsystem': ['mpfi', '2bbl', 'mfi', '1bbl', 'spfi', '4bbl', 'idi', 'spdi']
}

categorical_inputs = {}
for col in categorical_features:
    categorical_inputs[col] = st.selectbox(f'Select {col}', options=categorical_options[col])

# Predict button
if st.button('Predict Price'):
    # Combine all inputs
    all_inputs = {**numeric_inputs, **categorical_inputs}
    input_df = pd.DataFrame([all_inputs])
    
    # Process the input data
    processed_input = process_new_data(input_df)
    
    # Make prediction
    prediction = model.predict(processed_input)
    
    # Display the prediction
    st.success(f'The predicted car price is: ${prediction.item():.2f}')
    
    # Display the processed input (optional, for debugging)
    st.write("Processed Input:")
    st.write(processed_input)

# Instructions
st.sidebar.header('Instructions')
st.sidebar.info(
    'Fill in the car information in the input fields on the left. '
    'Click the "Predict Price" button to get the estimated car price.'
)

# About
st.sidebar.header('About')
st.sidebar.info(
    'This app predicts car prices based on various features. '
    'It uses a machine learning model trained on historical car data.'
)
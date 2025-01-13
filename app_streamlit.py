import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('Survival_model.pkl')

# Streamlit App
st.title("Survival Prediction App")

# Description
st.write("""
This application predicts whether a person will be saved from sinking based on the following factors:
- **Age**
- **Gender**
- **Socio-economic Status (Class)**
""")

# User Input Fields
age = st.slider("Age", min_value=1, max_value=100, value=25, step=1)
gender = st.radio("Gender", options=["Male", "Female"])
socio_economic_status = st.selectbox("Socio-economic Status", options=["1st Class", "2nd Class", "3rd Class"])

# Convert user inputs to model-compatible format
gender_encoded = 0 if gender == "Male" else 1
class_encoded = {"1st Class": 1, "2nd Class": 2, "3rd Class": 3}[socio_economic_status]

# Create feature array
input_features = np.array([[age, gender_encoded, class_encoded]])

# Predict Button
if st.button("Predict"):
    prediction = model.predict(input_features)
    result = "Saved" if prediction[0] == 1 else "Not Saved"
    st.success(f"The person will most likely be: **{result}**")

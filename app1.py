import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image
import base64
from io import BytesIO

# Load the model and expected features
with open("final2_model.pkl", "rb") as f:
    model, feature_columns = pickle.load(f)

# Header and Image
st.markdown("""
<h1 style='text-align: center;'> Car Price Prediction App</h1>
<hr style="border: none; height: 3px; background: linear-gradient(to right, #4CAF50, #2196F3, #9C27B0); margin-top: -10px; margin-bottom: 30px;">
""", unsafe_allow_html=True)

image = Image.open("car_image.jpg")
buffered = BytesIO()
image.resize((600, 210)).save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_str}"
             width="600" height="210"
             style="border-radius: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("Fill in the details below to estimate the resale price of your car.")
# Input fields
brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "BMW", "Audi", "Chevrolet", "Datsun"])
model_name = st.text_input("Model Name", "Swift")
car_age = st.slider("Car Age (in years)", 0, 30, 5)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# Label encode
fuel_map = {"Petrol": 3, "Diesel": 0, "CNG": 1, "LPG": 2, "Electric": 4}
seller_map = {"Individual": 1, "Dealer": 0, "Trustmark Dealer": 2}
trans_map = {"Manual": 1, "Automatic": 0}
owner_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2, "Fourth & Above Owner": 3, "Test Drive Car": 4}

# Construct raw DataFrame
data = {
    'km_driven': np.log1p(km_driven),
    'fuel': fuel_map[fuel],
    'seller_type': seller_map[seller_type],
    'transmission': trans_map[transmission],
    'owner': owner_map[owner],
    'Car_Age': car_age,
    'brand': brand,
    'model': model_name
}
df_input = pd.DataFrame([data])

# Apply one-hot encoding like training
df_input_encoded = pd.get_dummies(df_input)

# Add any missing columns with 0
for col in feature_columns:
    if col not in df_input_encoded:
        df_input_encoded[col] = 0

# Ensure order
df_input_encoded = df_input_encoded[feature_columns]

# Predict
if st.button("Predict Price 💰"):
    prediction = model.predict(df_input_encoded)[0]
    st.success(f"Estimated Selling Price: ₹ {prediction:,.2f}")
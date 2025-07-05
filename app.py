import streamlit as st
import pickle
import numpy as np

# Loading trained model
model = pickle.load(open('car_model1.pkl', 'rb'))

# Inject custom CSS for floating labels
st.markdown("""
<style>
.input-container {
  position: relative;
  margin-bottom: 20px;
}
.input-container input, .input-container select {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  outline: none;
  font-size: 16px;
  background: #1E1E2F;
}
.input-container label {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 0 5px;
  background: #f9f9f9;
  color: #999;
  transition: 0.2s;
  pointer-events: none;
}
.input-container input:focus + label,
.input-container input:not(:placeholder-shown) + label,
.input-container select:focus + label,
.input-container select:valid + label {
  top: -10px;
  left: 10px;
  font-size: 12px;
  color: #333;
  background: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center;'>Car Price Prediction App</h1>
<hr style="border: none; height: 3px; background: linear-gradient(to right, #4CAF50, #2196F3, #9C27B0); margin-top: -10px; margin-bottom: 30px;">
""", unsafe_allow_html=True)

import base64
from PIL import Image
import streamlit as st

# Load and resize the image
image = Image.open("car_image.jpg")
resized_image = image.resize((600, 210))

# Convert image to base64
from io import BytesIO
buffered = BytesIO()
resized_image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Inject centered image with rounded corners
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



# Inputs with floating placeholders
present_price = st.text_input(" ", placeholder="Current Ex-Showroom Price (in Lakhs)")
kms_driven = st.text_input(" ", placeholder="KMs Driven")
year = st.text_input(" ", placeholder="Year of Manufacture")

owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
transmission = st.selectbox("Transmission", ['Manual', 'Automatic'])

# Converting inputs
try:
    present_price = float(present_price)
except:
    present_price = 0.0

try:
    kms_driven = int(kms_driven)
except:
    kms_driven = 0

try:
    year = int(year)
except:
    year = 2025

car_age = 2025 - year

# Encoding categorical fields
fuel_dict = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
seller_dict = {'Dealer': 0, 'Individual': 1, 'Trustmark Dealer': 2}
trans_dict = {'Manual': 1, 'Automatic': 0}

input_features = np.array([[present_price, kms_driven, owner,
                            fuel_dict[fuel_type],
                            seller_dict[seller_type],
                            trans_dict[transmission],
                            car_age]])


# Add vertical spacing before the button
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# Centered Predict Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict = st.button("Predict Selling Price", use_container_width=True)

# Prediction logic
if predict:
    if present_price <= 0 or kms_driven <= 0:
        st.warning("❗ Please enter valid Present Price and KMs Driven.")
    else:
        prediction = model.predict(input_features)
        st.success(f"Estimated Selling Price: ₹{round(prediction[0], 2)} Lakhs")

# Add space between buttons
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([4, 1, 4])  # Narrower center
with col2:
    if st.button("Reset", key="reset"):
        st.experimental_rerun()


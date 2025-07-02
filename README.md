# Car Price Prediction Web App

This is a simple machine learning project that predicts the selling price of a used car based on various input features. It uses a trained model wrapped inside an interactive and clean web interface built with Streamlit.

The project focuses on usability, simplicity, and quick deployment — ideal for showcasing machine learning fundamentals and web integration.

---

## Problem Statement

Used car prices can vary significantly depending on many factors like how far the car has been driven, the type of fuel used, how old the car is, and more. Estimating the correct selling price can be challenging.

This project solves this problem using a machine learning model that predicts a fair selling price based on historical data and user input.

---

## Features Used for Prediction

- Current Ex-Showroom Price (in Lakhs)
- Kilometers Driven
- Year of Manufacture (used to calculate car age)
- Number of Previous Owners
- Fuel Type: Petrol, Diesel, or CNG
- Seller Type: Dealer, Individual, or Trustmark Dealer
- Transmission Type: Manual or Automatic

---

## Machine Learning Model

- **Model**: Random Forest Regressor
- **Libraries**: scikit-learn, pandas, numpy
- **Performance**:
  - Mean Absolute Error (MAE): ~16,733
  - Root Mean Squared Error (RMSE): ~388,461
  - R² Score: ~0.51

---

## Web App (Streamlit)

- Built using Python and Streamlit
- Interactive user interface with floating labels and form styling
- Inputs are validated and error-checked
- Prediction result is displayed instantly
- Includes a reset button and a styled header image

---

## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/Car-Price-Prediction.git
cd Car-Price-Prediction

2. Install the required Python packages:
```bash
pip install -r requirements.txt

3. Run the app using Streamlit:
```bash
streamlit run app.py

4. Project structure:

Car-Price-Prediction/
├── app.py                 # Streamlit web application
├── car_model1.pkl         # Trained ML model
├── car_image.jpg          # UI banner/header image
├── car_data.csv            # Original dataset (optional)
├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation

5. Future Improvements
   
    Add more vehicle attributes such as brand or engine size

    Improve model performance with more data or feature engineering

    Host the app publicly using Streamlit Cloud or other platforms

    Include login and history tracking features



** Author:
Nishant Bayaskar
Aspiring Data Scientist | Python & ML Enthusiast
LinkedIn: https://www.linkedin.com/in/your-profile
GitHub: https://github.com/your-username
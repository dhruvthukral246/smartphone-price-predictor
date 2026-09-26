import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("smartphone_price_model.pkl")

st.set_page_config(
    page_title="Smartphone Price Predictor",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Second-Hand Smartphone Price Predictor")

st.write(
    "Enter the smartphone details below to estimate its "
    "second-hand resale price."
)

# Input fields for the Streamlit app
brand = st.selectbox(
    "Brand",
    ["Samsung", "Apple", "OnePlus", "Xiaomi", "Vivo", "Oppo", "Realme"]
)

launch_price = st.number_input(
    "Original Launch Price (₹)",
    min_value=1000,
    max_value=300000,
    value=50000,
    step=1000
)

launch_year = st.number_input(
    "Launch Year",
    min_value=2015,
    max_value=2026,
    value=2023
)

age_years = st.number_input(
    "Phone Age (Years)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.5
)

city = st.selectbox(
    "City",
    ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer"]
)

ram = st.selectbox(
    "RAM (GB)",
    [2, 3, 4, 6, 8, 12, 16]
)

storage = st.selectbox(
    "Storage (GB)",
    [32, 64, 128, 256, 512, 1024]
)

processor = st.text_input(
    "Processor",
    "Snapdragon"
)

display_hz = st.selectbox(
    "Display Refresh Rate (Hz)",
    [60, 90, 120, 144, 165]
)

battery_health = st.slider(
    "Battery Health (%)",
    50,
    100,
    85
)

camera = st.number_input(
    "Camera (MP)",
    min_value=2,
    max_value=200,
    value=50
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Good", "Fair", "Poor"]
)

screen_crack = st.selectbox(
    "Screen Crack",
    ["No", "Yes"]
)

scratches = st.selectbox(
    "Scratches",
    ["None", "Minor", "Major"]
)

box = st.selectbox(
    "Original Box",
    ["Yes", "No"]
)

charger = st.selectbox(
    "Original Charger",
    ["Yes", "No"]
)

invoice = st.selectbox(
    "Invoice Available",
    ["Yes", "No"]
)

warranty = st.selectbox(
    "Warranty",
    ["Yes", "No"]
)

network = st.selectbox(
    "Network",
    ["4G", "5G"]
)

repair_history = st.selectbox(
    "Repair History",
    ["No", "Yes"]
)

# Prediction button
if st.button("🔮 Predict Resale Price"):

    # Create a DataFrame from the input data
    phone = pd.DataFrame({
        "brand": [brand],
        "launch_price_inr": [launch_price],
        "launch_year": [launch_year],
        "age_years": [age_years],
        "city": [city],
        "seller_type": [seller_type],
        "ram_gb": [ram],
        "storage_gb": [storage],
        "processor": [processor],
        "display_hz": [display_hz],
        "battery_health_pct": [battery_health],
        "camera_mp": [camera],
        "condition": [condition],
        "screen_crack": [screen_crack],
        "scratches": [scratches],
        "box": [box],
        "charger": [charger],
        "invoice": [invoice],
        "warranty": [warranty],
        "network": [network],
        "repair_history": [repair_history]
    })

    # Make prediction
    prediction = model.predict(phone)[0]

    # Display the prediction
    st.success(
        f"### Estimated Resale Price: ₹{prediction:,.0f}"
    )

    st.info(
        "This is an AI/ML-based estimate and may differ from "
        "actual marketplace prices."
    )

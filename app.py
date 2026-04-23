import streamlit as st
import pickle as pkl
import numpy as np

final_model = pkl.load(open('model.pkl', 'rb'))

d1 = {'Comprehensive': 0, 'Third Party insurance': 1, 'Third Party': 1, 'Zero Dep': 2, 'Not Available': 3}
d2 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}
d3 = {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Forth Owner': 4, 'Fifth Owner': 5}
d4 = {'Manual': 0, 'Automatic': 1}

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title('🚗 Car Price Prediction App')
st.markdown("Enter the car details below to estimate the resale price.")

st.subheader("Basic Details")
col1, col2 = st.columns(2)

with col1:
    val_insurance = st.selectbox('Insurance Validity', options=list(d1.keys()))
    val_fuel = st.selectbox('Fuel Type', options=list(d2.keys()))
    val_ownership = st.selectbox('Ownership', options=list(d3.keys()))

with col2:
    val_transmission = st.radio('Transmission', options=list(d4.keys()), horizontal=True)
    val_seats = st.selectbox('Seats', options=[4, 5, 6, 7, 8], index=1)
    val_year = st.slider('Manufacturing Year', min_value=2007, max_value=2023, value=2018, step=1)

st.subheader("Usage & Performance")
val_kms = st.slider('KMs Driven', min_value=0, max_value=200000, value=40000, step=1000)
val_mileage = st.slider('Mileage (kmpl)', min_value=5.0, max_value=35.0, value=18.0, step=0.5)

col3, col4 = st.columns(2)
with col3:
    val_engine = st.number_input('Engine (cc)', min_value=500, max_value=5000, value=1500, step=50)
with col4:
    val_power = st.number_input('Max Power (bhp)', min_value=50, max_value=500, value=100, step=5)

val_torque = st.number_input('Torque (Nm)', min_value=50, max_value=700, value=200, step=10)

st.markdown("---")

if st.button('💰 Predict Price', use_container_width=True):
    features = [[
        d1[val_insurance],
        d2[val_fuel],
        val_kms,
        d3[val_ownership],
        d4[val_transmission],
        val_year,
        val_mileage,
        val_engine,
        val_power,
        val_torque,
        val_seats
    ]]
    predicted_lakhs = final_model.predict(features)[0]
    predicted_lakhs = max(0.5, predicted_lakhs)  # floor at ₹0.5L

    st.success(f'### Estimated Price: ₹ {predicted_lakhs:.2f} Lakhs')
    st.info(f'≈ ₹ {predicted_lakhs * 100000:,.0f}')

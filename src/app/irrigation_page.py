import streamlit as st
import joblib
import numpy as np
import os
import sys
import plotly.express as px

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model = joblib.load(os.path.join(MODEL_PATH, "irrigation_model.pkl"))
crop_encoder = joblib.load(os.path.join(MODEL_PATH, "crop_encoder.pkl"))
irrigation_encoder = joblib.load(os.path.join(MODEL_PATH, "irrigation_encoder.pkl"))

def show_irrigation_page():
    st.subheader("🌾 Irrigation Efficiency Analysis")

    col1, col2 = st.columns(2)

    with col1:
        crop = st.selectbox("Select Crop", list(crop_encoder.classes_))

    with col2:
        irrigation = st.selectbox("Select Irrigation Type",
                                  list(irrigation_encoder.classes_))

    water_use = st.slider("Water Use (m³/kg)", 0, 5000, 1000)

    if st.button("🔍 Analyze Irrigation Efficiency"):
        crop_encoded = crop_encoder.transform([crop])[0]
        irrigation_encoded = irrigation_encoder.transform([irrigation])[0]

        X = np.array([[crop_encoded, water_use, irrigation_encoded]])
        prediction = model.predict(X)[0]

        if prediction == "Inefficient":
            st.error("🚨 Irrigation is Inefficient")
        else:
            st.success("✅ Irrigation is Efficient")

        # Water usage chart
        fig = px.bar(
            x=["Water Use"],
            y=[water_use],
            labels={"x": "Metric", "y": "Value"},
            title="Water Consumption Analysis"
        )

        st.plotly_chart(fig, use_container_width=True)

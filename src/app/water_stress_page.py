import streamlit as st
import joblib
import numpy as np
import os
import sys
import pandas as pd
import plotly.express as px

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from config import MODEL_PATH

model = joblib.load(os.path.join(MODEL_PATH, "water_stress_model.pkl"))

def show_water_page():
    st.subheader("💧 District Water Crisis Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        recharge = st.number_input("Annual Recharge", min_value=0.0)

    with col2:
        extraction = st.number_input("Annual Extraction", min_value=0.0)

    with col3:
        stage = st.slider("Extraction Stage (%)", 0, 200)

    if st.button("🔍 Predict Water Stress"):

        # Create input only when button is pressed
        X = np.array([[recharge, extraction, stage]])
        prediction = model.predict(X)[0]

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric("Recharge", recharge)

        with colB:
            st.metric("Extraction", extraction)

        with colC:
            st.metric("Extraction Stage (%)", stage)

        if prediction == "High":
            st.error(f"🚨 Water Stress Level: {prediction}")
        elif prediction == "Medium":
            st.warning(f"⚠️ Water Stress Level: {prediction}")
        else:
            st.success(f"✅ Water Stress Level: {prediction}")

        # Feature Importance Chart
        importance = model.feature_importances_
        features = ["Recharge", "Extraction", "Extraction Stage"]

        df_importance = pd.DataFrame({
            "Feature": features,
            "Importance": importance
        })

        fig = px.bar(
            df_importance,
            x="Feature",
            y="Importance",
            color="Feature",
            title="Model Feature Importance"
        )

        st.plotly_chart(fig, use_container_width=True)

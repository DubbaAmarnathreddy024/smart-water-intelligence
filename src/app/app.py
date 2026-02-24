import streamlit as st
from water_stress_page import show_water_page
from irrigation_page import show_irrigation_page

st.set_page_config(
    page_title="Smart Water Intelligence",
    layout="wide",
    page_icon="💧"
)

st.title("💧 Smart Water Crisis & Irrigation Intelligence System")
st.markdown("""
### AI-Powered Water Sustainability Dashboard  
Real-time analytics for groundwater stress and irrigation efficiency.
""")

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Select Module",
    ["Water Crisis Prediction", "Irrigation Efficiency", "About Project"]
)

if menu == "Water Crisis Prediction":
    show_water_page()

elif menu == "Irrigation Efficiency":
    show_irrigation_page()

elif menu == "About Project":
    st.subheader("📘 Project Overview")
    st.write("""
    This system predicts district-level water crisis risk and analyzes irrigation inefficiency 
    using machine learning models trained on real-world datasets.
    
    Modules:
    • Water Stress Prediction (Groundwater Data)
    • Irrigation Efficiency Analysis (Crop & Water Use Data)
    
    Technologies Used:
    • Python
    • Pandas
    • Scikit-Learn (Random Forest)
    • Streamlit
    • Plotly Visualization
    """)
    
    st.subheader("🚀 Future Scope")
    st.write("""
    • Rainfall forecasting using time-series models  
    • GIS-based district heatmaps  
    • Real-time sensor integration  
    • Government water policy support system  
    """)

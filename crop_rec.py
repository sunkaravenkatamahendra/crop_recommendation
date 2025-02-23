import streamlit as st
import google.generativeai as genai

genai.configure(api_key="Enter your Gemini_AI API Key")

def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    
    prompt = f"""
    Given the following soil and climate conditions:
    - Nitrogen (N): {N}
    - Phosphorus (P): {P}
    - Potassium (K): {K}
    - Temperature: {temperature}°C
    - Humidity: {humidity}%
    - pH Level: {ph}
    - Rainfall: {rainfall} mm

    Suggest the most suitable crop for farming in these conditions and provide a brief explanation.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text

st.title("Crop Recommendation System")

N = st.number_input("Enter Nitrogen (N)", min_value=0, max_value=200, value=90)
P = st.number_input("Enter Phosphorus (P)", min_value=0, max_value=200, value=42)
K = st.number_input("Enter Potassium (K)", min_value=0, max_value=200, value=43)
temperature = st.number_input("Enter Temperature (°C)", min_value=-50, max_value=50, value=22)
humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=80)
ph = st.number_input("Enter pH Level", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Enter Rainfall (mm)", min_value=0, max_value=500, value=200)

if st.button("Get Crop Recommendation"):
    recommendation = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.subheader("Recommended Crop:")
    st.write(recommendation)


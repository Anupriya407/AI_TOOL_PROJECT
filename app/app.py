import streamlit as st
import joblib
import pandas as pd
import warnings

# Hide warnings (clean output)
warnings.filterwarnings("ignore")

# Load correct model file (IMPORTANT FIX)
model = joblib.load("../model/study_model (1).pkl")

# Title
st.title("📚 AI Study Time Recommender")

st.write("Enter your study details:")

# Inputs
sleep = st.slider("Sleep Hours", 4, 10, 7)
focus = st.slider("Focus Level", 1, 10, 7)
free_time = st.slider("Free Time", 1, 10, 5)
days_left = st.slider("Days Left", 1, 15, 5)

# Prediction
if st.button("Recommend"):

    # FIX: use DataFrame (removes warning)
    input_data = pd.DataFrame([[sleep, focus, free_time, days_left]],
                              columns=['sleep_hours', 'focus_level', 'free_time', 'days_left'])

    prediction = model.predict(input_data)

    # Output
    st.success(f"📚 Recommended Study Time: {prediction[0]:.2f} hours/day")

    # Bonus insights
    if focus > 7:
        st.info("🔥 High focus detected — you can study efficiently")

    if days_left < 5:
        st.warning("⚠️ Exam is near — increase study time")

    if free_time < 3:
        st.warning("⚠️ Limited free time — optimize your schedule")

        
import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_recommendation(prediction,
                       scenario1,
                       scenario2,
                       scenario3):

    prompt = f"""
You are Carbon Twin AI.

Current predicted carbon footprint:
{prediction:.2f} kg CO2/month.

Scenario 1:
{scenario1:.2f} kg CO2

Scenario 2:
{scenario2:.2f} kg CO2

Scenario 3:
{scenario3:.2f} kg CO2

Choose the best scenario and explain:
1. Why it is best
2. Potential environmental impact
3. A short 30-day action plan

Keep the answer concise and personalized.
"""

    response = model.generate_content(prompt)
    return response.text
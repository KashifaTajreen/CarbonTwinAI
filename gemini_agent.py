import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_recommendation(
        prediction,
        scenario1,
        scenario2,
        scenario3):

    prompt=f"""
You are Carbon Twin AI.

Current predicted carbon footprint:
{prediction:.2f} kg CO2/month.

Scenario 1:
{scenario1:.2f}

Scenario 2:
{scenario2:.2f}

Scenario 3:
{scenario3:.2f}

Act like an intelligent sustainability coach.

Explain:
1. Biggest contributor.
2. Best scenario.
3. Money that could be saved.
4. Environmental impact.
5. A 30-day action plan.

Make it sound futuristic and personalized.
"""

    response=model.generate_content(prompt)

    return response.text
import streamlit as st
from calculator import calculate_carbon
from simulator import simulate_improvement
from predictor import train_model
from gemini_agent import get_recommendation

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Carbon Twin AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b,#0f766e);
}

h1, h2, h3, p, label {
    color: white !important;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 15px rgba(0,255,255,0.2);
}

div.stButton > button {
    background: linear-gradient(90deg,#06b6d4,#14b8a6);
    color: white;
    border-radius: 12px;
    border: none;
    height: 50px;
    width: 100%;
    font-size: 20px;
    font-weight: bold;
}

div[data-testid="stVerticalBlock"] {
    border-radius: 15px;
}

[data-testid="stMarkdownContainer"] {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.title("🌍 Carbon Twin AI")
st.caption(
    "A Generative Digital Twin that predicts your future carbon footprint and simulates greener lifestyles."
)

# ---------------- MODEL ---------------- #
model = train_model()

# ---------------- INPUTS ---------------- #
st.subheader("📝 Enter Your Lifestyle Data")

col1, col2 = st.columns(2)

with col1:
    car_km = st.number_input("🚗 Car Travel (km/month)", 0)
    bike_km = st.number_input("🏍 Bike Travel (km/month)", 0)
    meat_meals = st.number_input("🍗 Meat Meals/month", 0)
    electricity_units = st.number_input("⚡ Electricity Units/month", 0)
    clothes = st.number_input("👕 Clothes Purchased/month", 0)

with col2:
    bus_km = st.number_input("🚌 Bus Travel (km/month)", 0)
    metro_km = st.number_input("🚇 Metro Travel (km/month)", 0)
    veg_meals = st.number_input("🥗 Vegetarian Meals/month", 0)
    ac_hours = st.number_input("❄ AC Hours/day", 0)
    online_orders = st.number_input("📦 Online Orders/month", 0)
    plastic_items = st.number_input("♻ Plastic Items/month", 0)

# ---------------- BUTTON ---------------- #
if st.button("🌍 Generate My Carbon Twin"):

    user_data = {
        "car_km": car_km,
        "bike_km": bike_km,
        "bus_km": bus_km,
        "metro_km": metro_km,
        "meat_meals": meat_meals,
        "veg_meals": veg_meals,
        "electricity_units": electricity_units,
        "ac_hours": ac_hours,
        "clothes": clothes,
        "online_orders": online_orders,
        "plastic_items": plastic_items
    }

    # Carbon calculator
    total = calculate_carbon(user_data)


    # RandomForest prediction

    future_change = model.predict(
        [[
        car_km,
        meat_meals,
        electricity_units,
        online_orders
    ]]

    )[0]

    prediction = total + (future_change * 0.15)

    # Future scenarios
    scenario1 = model.predict([[
        car_km * 0.7,
        meat_meals,
        electricity_units,
        online_orders
    ]])[0]

    scenario2 = model.predict([[
        car_km,
        meat_meals * 0.5,
        electricity_units,
        online_orders
    ]])[0]

    scenario3 = model.predict([[
        car_km * 0.5,
        meat_meals * 0.5,
        electricity_units * 0.8,
        online_orders
    ]])[0]

    # Sustainability score
    score = max(0, 100 - int(prediction / 5))

    # Simulator
    improved, saved = simulate_improvement(total)

    # ---------------- METRICS ---------------- #
    st.subheader("📊 Carbon Twin Dashboard")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "🌍 Current Footprint",
            f"{total:.2f} kg CO₂/month"
        )

    with m2:
        st.metric(
            "🔮 Predicted Next Month",
            f"{prediction:.2f} kg CO₂"
        )

    with m3:
        st.metric(
            "🌱 Sustainability Score",
            f"{score}/100"
        )

    st.progress(score / 100)

    if score > 80:
        st.balloons()

    # ---------------- SCENARIOS ---------------- #
    st.subheader("🔮 Future Lifestyle Simulations")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "🚇 Public Transport Shift",
            f"{scenario1:.2f} kg"
        )

    with s2:
        st.metric(
            "🥗 Reduced Meat Consumption",
            f"{scenario2:.2f} kg"
        )

    with s3:
        st.metric(
            "🌱 Green Lifestyle Mode",
            f"{scenario3:.2f} kg"
        )

    # ---------------- AGENT ANALYSIS ---------------- #
    st.subheader("🤖 AI Agent Analysis")


    # ---------------- SIMULATION RESULT ---------------- #
    st.subheader("🌱 What-if Simulator")

    st.success(
        f"If you follow the recommendations, your footprint could become "
        f"{improved:.2f} kg CO₂/month.\n\n"
        f"Potential Reduction: {saved:.2f} kg CO₂/month."
    )

    # ---------------- GEMINI AGENT ---------------- #
    st.subheader("🧠 Gemini Sustainability Coach")

    with st.spinner("Generating your personalized sustainability roadmap..."):
        advice = get_recommendation(
            prediction,
            scenario1,
            scenario2,
            scenario3
        )

    st.markdown(advice)
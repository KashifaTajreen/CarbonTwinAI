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

# ---------------- CSS ---------------- #
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b,#0f766e);
}

h1,h2,h3,p,label {
    color:white !important;
}

div[data-testid="stMetric"]{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
}

div.stButton > button{
    background:linear-gradient(90deg,#06b6d4,#14b8a6);
    color:white;
    border:none;
    border-radius:12px;
    height:50px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MODEL CACHING ---------------- #
@st.cache_resource
def load_model():
    return train_model()

model = load_model()

# ---------------- TITLE ---------------- #
st.title("🌍 Carbon Twin AI")
st.caption(
    "A Generative Digital Twin for understanding, tracking and reducing personal carbon footprint."
)

st.markdown("""
### How to Use

1. Enter your lifestyle information.
2. Generate your Digital Carbon Twin.
3. Explore future scenarios.
4. Receive AI-powered sustainability recommendations.

This platform helps individuals understand, track and reduce their carbon footprint through simple actions and personalized insights.
""")

# ---------------- INPUTS ---------------- #
st.subheader("📝 Lifestyle Inputs")

col1, col2 = st.columns(2)

with col1:
    car_km = st.number_input(
        "🚗 Car Travel (km/month)",
        0,
        help="Approximate monthly distance travelled by car."
    )

    bike_km = st.number_input(
        "🏍 Bike Travel (km/month)",
        0
    )

    meat_meals = st.number_input(
        "🍗 Meat Meals/month",
        0,
        help="Number of meat-based meals consumed per month."
    )

    electricity_units = st.number_input(
        "⚡ Electricity Units/month",
        0,
        help="Approximate monthly electricity consumption."
    )

    clothes = st.number_input(
        "👕 Clothes Purchased/month",
        0
    )

with col2:
    bus_km = st.number_input(
        "🚌 Bus Travel (km/month)",
        0
    )

    metro_km = st.number_input(
        "🚇 Metro Travel (km/month)",
        0
    )

    veg_meals = st.number_input(
        "🥗 Vegetarian Meals/month",
        0
    )

    ac_hours = st.number_input(
        "❄ AC Hours/day",
        0
    )

    online_orders = st.number_input(
        "📦 Online Orders/month",
        0,
        help="Approximate number of online orders placed monthly."
    )

    plastic_items = st.number_input(
        "♻ Plastic Items/month",
        0
    )

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

    # Current footprint
    total = calculate_carbon(user_data)

    # RandomForest prediction
    rf_prediction = model.predict([[
        car_km,
        meat_meals,
        electricity_units,
        online_orders
    ]])[0]

    # Keep prediction realistic
    prediction = total + (rf_prediction * 0.15)

    # Scenarios
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
    score = max(0, min(100, int(100 - prediction / 5)))

    improved, saved = simulate_improvement(total)

    # ---------------- DASHBOARD ---------------- #
    st.subheader("📊 Carbon Twin Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🌍 Current Footprint",
            f"{total:.2f} kg CO₂"
        )

    with c2:
        st.metric(
            "🔮 Predicted Future",
            f"{prediction:.2f} kg CO₂"
        )

    with c3:
        st.metric(
            "🌱 Sustainability Score",
            f"{score}/100"
        )

    st.progress(score / 100)

    # ---------------- SCENARIOS ---------------- #
    st.subheader("🔮 Future Simulations")

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

    # ---------------- IMPACT ---------------- #
    reduction = prediction - min(
        scenario1,
        scenario2,
        scenario3
    )

    trees = reduction / 22

    i1, i2 = st.columns(2)

    with i1:
        st.metric(
            "♻ Potential Reduction",
            f"{reduction:.1f} kg CO₂"
        )

    with i2:
        st.metric(
            "🌳 Trees Equivalent",
            f"{trees:.1f}"
        )

    # ---------------- SIMULATOR ---------------- #
    st.subheader("🌱 What-if Simulator")

    st.success(
        f"If recommendations are followed, your footprint could become "
        f"{improved:.2f} kg CO₂/month.\n\n"
        f"Potential reduction: {saved:.2f} kg CO₂/month."
    )

    # ---------------- GEMINI ---------------- #
    st.subheader("🧠 Gemini Sustainability Coach")

    try:
        with st.spinner(
            "Generating personalized sustainability roadmap..."
        ):
            advice = get_recommendation(
                prediction,
                scenario1,
                scenario2,
                scenario3
            )

        st.markdown(advice)

    except Exception:
        st.warning(
            "Unable to generate Gemini recommendations right now."
        )

    # ---------------- ALIGNMENT ---------------- #
    st.info(
        "Carbon Twin AI helps individuals understand, track and reduce their carbon footprint through simple actions and personalized insights using Machine Learning and Generative AI."
    )
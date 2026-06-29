import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------
# Load Model
# ---------------------------------------

model = joblib.load("models/business_recommendation_model.pkl")
encoders = joblib.load("models/label_encoders.pkl")

st.set_page_config(
    page_title="AI Business Recommendation System",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI-Powered Business Recommendation System")

st.write(
    "Enter business information below to receive the most suitable digital service recommendation."
)

# ---------------------------------------
# User Inputs
# ---------------------------------------

industry = st.selectbox(
    "Industry",
    encoders["Industry"].classes_
)

business_size = st.selectbox(
    "Business Size",
    encoders["Business Size"].classes_
)

website = st.selectbox(
    "Existing Website",
    encoders["Website"].classes_
)

social_media = st.selectbox(
    "Social Media Presence",
    encoders["Social Media"].classes_
)

seo_score = st.slider(
    "SEO Score",
    0,
    100,
    50
)

budget = st.number_input(
    "Marketing Budget",
    min_value=1000,
    max_value=1000000,
    value=100000,
    step=1000
)

goal = st.selectbox(
    "Business Goal",
    encoders["Goal"].classes_
)

# ---------------------------------------
# Feature Engineering
# ---------------------------------------

if budget < 50000:
    budget_category = "Low"
elif budget < 200000:
    budget_category = "Medium"
else:
    budget_category = "High"

# Encode Inputs

industry = encoders["Industry"].transform([industry])[0]

business_size = encoders["Business Size"].transform([business_size])[0]

website = encoders["Website"].transform([website])[0]

social_media = encoders["Social Media"].transform([social_media])[0]

goal = encoders["Goal"].transform([goal])[0]

budget_category = encoders["Budget Category"].transform([budget_category])[0]

# ---------------------------------------
# Prediction
# ---------------------------------------

if st.button("Predict Recommendation"):

    input_data = pd.DataFrame(
        [[
            industry,
            business_size,
            website,
            social_media,
            seo_score,
            budget,
            goal,
            budget_category
        ]],
        columns=[
            "Industry",
            "Business Size",
            "Website",
            "Social Media",
            "SEO Score",
            "Budget",
            "Goal",
            "Budget Category"
        ]
    )

    prediction = model.predict(input_data)

    service = encoders["Recommended Service"].inverse_transform(prediction)

    st.success(f"Recommended Service: {service[0]}")
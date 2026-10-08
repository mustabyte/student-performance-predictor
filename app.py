import streamlit as st
import pandas as pd
import joblib
import math

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

model = joblib.load("model/student_model.pkl")

st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's information below to predict their expected exam score."
)

st.subheader("Student Information")

col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "Hours Studied",
        min_value=1,
        max_value=44,
        value=20
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=60,
        max_value=100,
        value=80
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=4,
        max_value=10,
        value=7
    )

    previous_scores = st.number_input(
        "Previous Score",
        min_value=50,
        max_value=100,
        value=75
    )

    tutoring_sessions = st.number_input(
        "Tutoring Sessions",
        min_value=0,
        max_value=8,
        value=1
    )

    physical_activity = st.number_input(
        "Physical Activity",
        min_value=0,
        max_value=6,
        value=3
    )


with col2:
    parental_involvement = st.selectbox(
        "Parental Involvement",
        ["Low", "Medium", "High"]
    )

    access_to_resources = st.selectbox(
        "Access to Resources",
        ["Low", "Medium", "High"]
    )

    extracurricular_activities = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

    motivation_level = st.selectbox(
        "Motivation Level",
        ["Low", "Medium", "High"]
    )

    internet_access = st.selectbox(
        "Internet Access",
        ["No", "Yes"]
    )

    family_income = st.selectbox(
        "Family Income",
        ["Low", "Medium", "High"]
    )

col3, col4 = st.columns(2)

with col3:
    teacher_quality = st.selectbox(
        "Teacher Quality",
        ["Low", "Medium", "High"]
    )

    school_type = st.selectbox(
        "School Type",
        ["Public", "Private"]
    )

    peer_influence = st.selectbox(
        "Peer Influence",
        ["Negative", "Neutral", "Positive"]
    )

    learning_disabilities = st.selectbox(
        "Learning Disabilities",
        ["No", "Yes"]
    )


with col4:
    parental_education_level = st.selectbox(
        "Parental Education Level",
        ["High School", "College", "Postgraduate"]
    )

    distance_from_home = st.selectbox(
        "Distance from Home",
        ["Near", "Moderate", "Far"]
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )


st.divider()

predict_button = st.button(
    "Predict Exam Score",
    type="primary",
    use_container_width=True
)

if predict_button:

    student_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Extracurricular_Activities": [extracurricular_activities],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Motivation_Level": [motivation_level],
        "Internet_Access": [internet_access],
        "Tutoring_Sessions": [tutoring_sessions],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "School_Type": [school_type],
        "Peer_Influence": [peer_influence],
        "Physical_Activity": [physical_activity],
        "Learning_Disabilities": [learning_disabilities],
        "Parental_Education_Level": [parental_education_level],
        "Distance_from_Home": [distance_from_home],
        "Gender": [gender]
    })

    prediction = float(model.predict(student_data)[0])

    if not math.isfinite(prediction):
        st.error("Unable to generate a valid prediction.")

    elif not 0 <= prediction <= 100:
        st.warning(f"Predicted score {prediction:.2f} is outside the expected range of 0–100.")

    else:
        st.success(f"Predicted Exam Score: {prediction:.2f}")
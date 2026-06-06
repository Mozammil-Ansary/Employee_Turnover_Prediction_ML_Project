import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/employee_turnover_rf_model.pkl", "rb"))

# Title
st.title("Employee Turnover Prediction")

st.write("Predict whether an employee is likely to leave the company.")

# Numerical Inputs
satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)

last_evaluation = st.slider("Last Evaluation", 0.0, 1.0, 0.5)

number_project = st.number_input("Number of Projects", 1, 10, 3)

average_montly_hours = st.number_input("Average Monthly Hours", 50, 400, 200)

time_spend_company = st.number_input("Years at Company", 1, 20, 3)

Work_accident = st.selectbox("Work Accident", [0, 1])

promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])

# Department
department = st.selectbox(
    "Department",
    [
        "IT",
        "RandD",
        "accounting",
        "hr",
        "management",
        "marketing",
        "product_mng",
        "support",
        "technical"
    ]
)

# Salary
salary = st.selectbox(
    "Salary Level",
    ["low", "medium", "high"]
)

# Prediction
if st.button("Predict"):

    # Department Encoding
    sales_IT = 1 if department == "IT" else 0
    sales_RandD = 1 if department == "RandD" else 0
    sales_accounting = 1 if department == "accounting" else 0
    sales_hr = 1 if department == "hr" else 0
    sales_management = 1 if department == "management" else 0
    sales_marketing = 1 if department == "marketing" else 0
    sales_product_mng = 1 if department == "product_mng" else 0
    sales_support = 1 if department == "support" else 0
    sales_technical = 1 if department == "technical" else 0

    # Salary Encoding
    salary_low = 1 if salary == "low" else 0
    salary_medium = 1 if salary == "medium" else 0

    # Final Feature Array
    features = np.array([[

        satisfaction_level,
        last_evaluation,
        number_project,
        average_montly_hours,
        time_spend_company,
        Work_accident,
        promotion_last_5years,

        sales_IT,
        sales_RandD,
        sales_accounting,
        sales_hr,
        sales_management,
        sales_marketing,
        sales_product_mng,
        sales_support,
        sales_technical,

        salary_low,
        salary_medium
    ]])

    # Prediction
    prediction = model.predict(features)

    # Output
    if prediction[0] == 1:
        st.error("Employee is likely to leave the company.")
    else:
        st.success("Employee is likely to stay in the company.")
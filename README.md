# 🚀 Employee Turnover Prediction (ML Project)
📌 **Project Overview**

Employee attrition is a major challenge for organizations. This project aims to predict whether an employee will leave the company based on various factors such as satisfaction level, number of projects, working hours, and more or he will stay.

Using Machine Learning techniques, I build a predictive model that helps HR departments take proactive decisions to reduce employee turnover.

**🎯 Objectives**
- Analyze employee data to understand key factors behind attrition
- Perform Exploratory Data Analysis (EDA)
- Build and evaluate classification models
- Predict employee turnover with high accuracy

**📂 Dataset Information**
Dataset Name: HR_comma_sep.csv
Contains employee-related features:
Satisfaction Level
Last Evaluation Score
Number of Projects
Average Monthly Hours
Time Spent in Company
Work Accident
Promotion Last 5 Years
Department
Salary

**🎯 Target Variable**
`left`
- 0 → Employee stays
- 1 → Employee leaves

**🛠️ Tech Stack**
- Programming Language: Python 🐍
- Libraries Used:
   - NumPy
   - Pandas
   - Matplotlib
   - Seaborn

**🔍 Exploratory Data Analysis (EDA)**
- Checked dataset shape and structure
- Verified missing values (No missing data found ✅)
- Correlation Heatmap to identify key relationships
- Distribution plots for feature understanding

**📊 Key Insights**
- Low satisfaction level strongly leads to attrition
- High working hours increase turnover probability
- Employees with more projects show higher churn risk

**⚙️ Data Preprocessing**
- Handled categorical variables
- Feature selection
- Data scaling using StandardScaler
- Train-Test split

**🤖 Machine Learning Models**
- The following models were used:
   - Logistic Regression
   - Random Forest classifier
   - Gradient Boosting classifier
   - K-means Clustering

**📈 Model Evaluation**
- Confusion Matrix
- Classification Report
- ROC Curve
- AUC Score


**📊 Visualizations Included**
- Correlation Heatmap
- Distribution Plots
- ROC Curve

**🧠 Key Learnings**
- Importance of EDA before modeling
- Feature relationships impact predictions heavily
- Model evaluation metrics are crucial beyond accuracy

**🚀 How to Run the Project**
1️⃣ *Clone the repository*
git clone https://github.com/your-username/employee-turnover-prediction.git

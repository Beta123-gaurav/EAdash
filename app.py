import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configure Streamlit page
st.set_page_config(page_title="Employee Attrition Insights", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("EA.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
departments = st.sidebar.multiselect("Select Department", options=df['Department'].unique(), default=df['Department'].unique())
genders = st.sidebar.multiselect("Select Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
age_range = st.sidebar.slider("Select Age Range", int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())))

filtered_df = df[
    (df['Department'].isin(departments)) &
    (df['Gender'].isin(genders)) &
    (df['Age'].between(age_range[0], age_range[1]))
]

# Title
st.title("📊 Employee Attrition Dashboard")
st.markdown("""
This interactive dashboard provides macro and micro-level insights about employee attrition to support HR decisions.
""")

# 1
st.markdown("### 1. Overall Attrition Rate")
st.markdown("This pie chart shows the proportion of employees who left versus those who stayed.")
fig1 = px.pie(filtered_df, names="Attrition")
st.plotly_chart(fig1, use_container_width=True)

# 2
st.markdown("### 2. Attrition by Department")
st.markdown("Bar chart displaying attrition counts across departments.")
fig2 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig2, use_container_width=True)

# 3
st.markdown("### 3. Attrition by Job Role")
st.markdown("Bar chart showing attrition distribution across job roles.")
fig3 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig3, use_container_width=True)

# 4
st.markdown("### 4. Attrition by Gender")
st.markdown("This shows how attrition varies by gender.")
fig4 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
st.plotly_chart(fig4, use_container_width=True)

# 5
st.markdown("### 5. Attrition by Age")
st.markdown("Histogram showing how age relates to attrition.")
fig5 = px.histogram(filtered_df, x="Age", color="Attrition", nbins=20, barmode="group")
st.plotly_chart(fig5, use_container_width=True)

# 6
st.markdown("### 6. Monthly Income Distribution")
st.markdown("Boxplot of monthly income grouped by attrition status.")
fig6 = px.box(filtered_df, x="Attrition", y="MonthlyIncome")
st.plotly_chart(fig6, use_container_width=True)

# 7
st.markdown("### 7. Education Field vs Attrition")
st.markdown("Shows attrition counts by education field.")
fig7 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
st.plotly_chart(fig7, use_container_width=True)

# 8
st.markdown("### 8. Overtime vs Attrition")
st.markdown("Bar chart comparing overtime status to attrition.")
fig8 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
st.plotly_chart(fig8, use_container_width=True)

# 9
st.markdown("### 9. Work-Life Balance vs Attrition")
st.markdown("This heatmap shows the relationship between work-life balance and attrition.")
pivot9 = pd.crosstab(filtered_df['WorkLifeBalance'], filtered_df['Attrition'])
fig9 = px.imshow(pivot9, text_auto=True, color_continuous_scale='Blues')
st.plotly_chart(fig9, use_container_width=True)

# 10
st.markdown("### 10. Years at Company vs Attrition")
st.markdown("Line chart showing years at company against attrition.")
fig10 = px.histogram(filtered_df, x="YearsAtCompany", color="Attrition", barmode="group", nbins=15)
st.plotly_chart(fig10, use_container_width=True)

# 11
st.markdown("### 11. Total Working Years vs Attrition")
st.markdown("Distribution of total working years colored by attrition.")
fig11 = px.histogram(filtered_df, x="TotalWorkingYears", color="Attrition", barmode="group", nbins=15)
st.plotly_chart(fig11, use_container_width=True)

# 12
st.markdown("### 12. Years Since Last Promotion")
st.markdown("Boxplot to visualize years since last promotion vs attrition.")
fig12 = px.box(filtered_df, x="Attrition", y="YearsSinceLastPromotion")
st.plotly_chart(fig12, use_container_width=True)

# 13
st.markdown("### 13. Marital Status vs Attrition")
st.markdown("See if marital status influences attrition.")
fig13 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
st.plotly_chart(fig13, use_container_width=True)

# 14
st.markdown("### 14. Job Involvement vs Attrition")
st.markdown("Job involvement levels against attrition status.")
fig14 = px.histogram(filtered_df, x="JobInvolvement", color="Attrition", barmode="group")
st.plotly_chart(fig14, use_container_width=True)

# 15
st.markdown("### 15. Performance Rating vs Attrition")
st.markdown("This shows if performance ratings affect attrition.")
fig15 = px.histogram(filtered_df, x="PerformanceRating", color="Attrition", barmode="group")
st.plotly_chart(fig15, use_container_width=True)

# 16
st.markdown("### 16. Years in Current Role")
st.markdown("Years in current role distribution by attrition.")
fig16 = px.histogram(filtered_df, x="YearsInCurrentRole", color="Attrition", barmode="group", nbins=15)
st.plotly_chart(fig16, use_container_width=True)

# 17
st.markdown("### 17. Relationship Satisfaction vs Attrition")
st.markdown("How relationship satisfaction might influence attrition.")
fig17 = px.histogram(filtered_df, x="RelationshipSatisfaction", color="Attrition", barmode="group")
st.plotly_chart(fig17, use_container_width=True)

# 18
st.markdown("### 18. Environment Satisfaction vs Attrition")
st.markdown("Shows environment satisfaction grouped by attrition.")
fig18 = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition", barmode="group")
st.plotly_chart(fig18, use_container_width=True)

# 19
st.markdown("### 19. Distance from Home vs Attrition")
st.markdown("Histogram showing distance from home by attrition status.")
fig19 = px.histogram(filtered_df, x="DistanceFromHome", color="Attrition", nbins=15, barmode="group")
st.plotly_chart(fig19, use_container_width=True)

# 20
st.markdown("### 20. Interactive Data Table")
st.markdown("Use the interactive data table to explore employee details with filters applied.")
st.dataframe(filtered_df)

# Footer
st.markdown("""
---
✅ This dashboard is built to help HR Directors and stakeholders gain 360° views on employee attrition factors.
""")

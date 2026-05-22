import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(page_title="EduPro Instructor Evaluation", layout="wide")
st.title("📊 Instructor Performance & Course Quality Evaluation – EduPro")

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    teachers = pd.read_csv("data/Teachers.csv")
    courses = pd.read_csv("data/courses.csv")
    transactions = pd.read_csv("data/Transactions.csv")
    return teachers, courses, transactions

teachers, courses, transactions = load_data()

# -------------------------
# Data Integration
# -------------------------
merged = transactions.merge(teachers, on="TeacherID", how="left")
merged = merged.merge(courses, on="CourseID", how="left")

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("🔍 Filters")

expertise_filter = st.sidebar.multiselect(
    "Select Expertise",
    options=merged["Expertise"].unique(),
    default=merged["Expertise"].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Course Category",
    options=merged["CourseCategory"].unique(),
    default=merged["CourseCategory"].unique()
)

rating_range = st.sidebar.slider(
    "Teacher Rating Range",
    min_value=float(merged["TeacherRating"].min()),
    max_value=float(merged["TeacherRating"].max()),
    value=(float(merged["TeacherRating"].min()), float(merged["TeacherRating"].max()))
)

filtered = merged[
    (merged["Expertise"].isin(expertise_filter)) &
    (merged["CourseCategory"].isin(category_filter)) &
    (merged["TeacherRating"].between(rating_range[0], rating_range[1]))
]

# -------------------------
# KPIs
# -------------------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Teacher Rating", round(filtered["TeacherRating"].mean(), 2))
col2.metric("Avg Course Rating", round(filtered["CourseRating"].mean(), 2))
col3.metric("Avg Experience (Years)", round(filtered["YearsOfExperience"].mean(), 1))
col4.metric("Total Enrollments", filtered.shape[0])

# -------------------------
# Instructor Leaderboard
# -------------------------
st.subheader("🏆 Instructor Performance Leaderboard")

leaderboard = (
    filtered.groupby("TeacherName")
    .agg({
        "TeacherRating": "mean",
        "CourseRating": "mean",
        "TransactionID": "count"
    })
    .rename(columns={"TransactionID": "Enrollments"})
    .sort_values("TeacherRating", ascending=False)
)

st.dataframe(leaderboard)

# -------------------------
# Experience vs Teacher Rating
# -------------------------
st.subheader("📈 Experience vs Instructor Rating")

fig1, ax1 = plt.subplots()
sns.scatterplot(
    data=filtered,
    x="YearsOfExperience",
    y="TeacherRating",
    hue="Expertise",
    ax=ax1
)
ax1.set_xlabel("Years of Experience")
ax1.set_ylabel("Teacher Rating")
st.pyplot(fig1)

# -------------------------
# Teacher Rating vs Course Rating
# -------------------------
st.subheader("📊 Teacher Rating vs Course Rating")

fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=filtered,
    x="TeacherRating",
    y="CourseRating",
    hue="CourseLevel",
    ax=ax2
)
ax2.set_xlabel("Teacher Rating")
ax2.set_ylabel("Course Rating")
st.pyplot(fig2)

# -------------------------
# Course Quality Heatmap
# -------------------------
st.subheader("🔥 Course Quality Heatmap")

heatmap_data = filtered.pivot_table(
    index="CourseCategory",
    columns="CourseLevel",
    values="CourseRating",
    aggfunc="mean"
)

fig3, ax3 = plt.subplots()
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", ax=ax3)
st.pyplot(fig3)

# -------------------------
# Expertise-wise Performance
# -------------------------
st.subheader("🎓 Expertise-wise Course Quality")

fig4, ax4 = plt.subplots()
sns.boxplot(
    data=filtered,
    x="Expertise",
    y="CourseRating",
    ax=ax4
)
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
st.pyplot(fig4)

# -------------------------
# Enrollment Influence
# -------------------------
st.subheader("📌 Enrollment Influence by Instructor Rating")

filtered["RatingTier"] = pd.cut(
    filtered["TeacherRating"],
    bins=[0, 3, 4, 5],
    labels=["Low", "Medium", "High"]
)

tier_enrollments = filtered.groupby("RatingTier")["TransactionID"].count()

fig5, ax5 = plt.subplots()
tier_enrollments.plot(kind="bar", ax=ax5)
ax5.set_ylabel("Enrollments")
st.pyplot(fig5)
# Instructor Performance and Course Quality Evaluation on EduPro

## 📌 Project Overview
Online education platforms rely heavily on instructor quality and course design to ensure learner satisfaction and platform credibility.  
This project presents a **data-driven evaluation framework** for analyzing **instructor performance** and **course quality** on the EduPro platform.

The analysis helps identify:
- High-performing instructors
- Quality consistency across courses
- The impact of teaching experience on learner satisfaction
- Expertise areas that require improvement

---

## 🎯 Problem Statement
EduPro currently lacks a structured mechanism to evaluate instructor effectiveness and course quality.  
Without systematic analysis, instructor assessment remains subjective and fragmented, making it difficult to ensure consistent educational standards.

---

## 🎯 Objectives
- Analyze the distribution of instructor ratings
- Study the relationship between teaching experience and performance
- Evaluate course quality across categories and levels
- Measure instructor impact on course success and enrollments
- Identify expertise domains with consistently high or low performance

---

## 📂 Dataset Description
The project uses three datasets stored in CSV format:

### 1️⃣ Teachers Dataset
- TeacherID  
- TeacherName  
- Age  
- Gender  
- Expertise  
- YearsOfExperience  
- TeacherRating  

### 2️⃣ Courses Dataset
- CourseID  
- CourseName  
- CourseCategory  
- CourseLevel  
- CourseRating  

### 3️⃣ Transactions Dataset
- TransactionID  
- CourseID  
- TeacherID  

---

## 🔍 Key Analytical Questions
- What is the overall distribution of instructor ratings?
- Do experienced instructors receive higher ratings?
- Is there a correlation between teacher ratings and course ratings?
- Which expertise areas consistently deliver high-quality courses?
- Are highly rated instructors associated with higher enrollments?

---

## 📊 Key Performance Indicators (KPIs)
| KPI Name | Description |
|--------|------------|
| Average Teacher Rating | Measures overall teaching quality |
| Average Course Rating | Evaluates content effectiveness |
| Rating Consistency Index | Instructor reliability indicator |
| Experience Impact Score | Effect of teaching tenure |
| Enrollment Influence Ratio | Instructor-driven demand |

---

## 🧠 Analytical Methodology
1. **Data Integration**
   - Joined Teachers, Courses, and Transactions using TeacherID and CourseID

2. **Instructor Profile Analysis**
   - Age, experience, expertise, and rating distribution

3. **Experience vs Performance**
   - Correlation analysis between experience and ratings

4. **Course Quality Evaluation**
   - Course ratings by category and level

5. **Instructor Impact Analysis**
   - Comparison of course ratings and enrollments across instructor tiers

6. **Expertise-Based Insights**
   - Performance evaluation across teaching domains

---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

---

## ▶️ How to Run the Project

### Step 1: Clone the repository
```bash
git clone <your-github-repo-link>
cd EduPro-Instructor-Evaluation

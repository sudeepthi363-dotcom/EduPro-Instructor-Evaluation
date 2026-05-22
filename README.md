# Instructor Performance and Course Quality Evaluation on EduPro

## 📌 Project Overview
This project presents a data-driven analytical framework to evaluate instructor performance and course quality on the EduPro online learning platform. The analysis focuses on understanding how instructor experience, expertise, and teaching quality influence course ratings and learner enrollments.

The project uses structured datasets and interactive visualizations to help stakeholders objectively identify high-performing instructors, quality gaps, and areas for improvement.

---

## 🎯 Objectives
- To evaluate instructor effectiveness using teacher ratings and experience
- To analyze the relationship between instructor ratings and course ratings
- To identify expertise areas that consistently deliver high-quality courses
- To study the impact of instructor quality on course enrollments
- To provide a transparent and data-driven evaluation system

---

## 🗂️ Dataset Description
The project uses three CSV datasets:

### 1. Teachers Dataset (`teacher.csv`)
- TeacherID  
- TeacherName  
- Age  
- Gender  
- Expertise  
- YearsOfExperience  
- TeacherRating  

### 2. Courses Dataset (`courses.csv`)
- CourseID  
- CourseName  
- CourseCategory  
- CourseLevel  
- CourseRating  

### 3. Transactions Dataset (`transaction.csv`)
- TransactionID  
- CourseID  
- TeacherID  

All datasets are integrated using **TeacherID** and **CourseID**.

---

## 🔍 Key Analysis Performed
- Distribution analysis of instructor ratings
- Experience vs instructor performance analysis
- Correlation between instructor ratings and course ratings
- Course quality analysis across categories and levels
- Expertise-wise performance comparison
- Enrollment analysis based on instructor rating tiers

---

## 📊 Key Performance Indicators (KPIs)
- Average Teacher Rating  
- Average Course Rating  
- Rating Consistency Index  
- Experience Impact Score  
- Enrollment Influence Ratio  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- Streamlit  
- Matplotlib  
- Seaborn  

---

## 💻 How to Run the Project
1. Install the required libraries:
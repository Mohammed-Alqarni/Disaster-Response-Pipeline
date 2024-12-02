# **Disaster Response Pipeline Project**

## **Table of Contents**
- [Overview](#overview)
- [File Structure](#file-structure)
- [Key Components](#key-components)
- [How to Use the Project](#how-to-use-the-project)
- [Credits and Acknowledgments](#credits-and-acknowledgments)
- [References](#references)

---

## **Overview**
This project focuses on building a disaster response classification system. It processes and analyzes real-world messages sent during emergencies to predict their relevance to specific disaster categories. The system is designed to help disaster relief agencies prioritize and allocate resources effectively.

The project includes:
- A pipeline to clean and store data in a structured format.
- A machine learning model to classify messages into multiple categories.
- An interactive web application for real-time message classification and data visualization.

---

## **File Structure**

**Application**  
- Templates for the web app interface (main and results pages).  
- A Python script to run the Flask application.

**Data Processing**  
- Datasets containing disaster messages and categories.  
- A script for preprocessing and storing data in an SQLite database.

**Model Training**  
- A script to train a multi-label classification model.  
- A serialized file containing the trained machine learning model.

**Documentation**  
- This README file.

---

## **Key Components**

### **1. Data Preparation Pipeline**
Cleans and organizes raw data, merging disaster messages and their corresponding categories into a usable format. The cleaned data is stored in a structured SQLite database for further use.

### **2. Machine Learning Pipeline**
Uses the cleaned data to train a machine learning model capable of classifying messages into multiple categories. The pipeline integrates text preprocessing, tokenization, and a classification algorithm.

### **3. Interactive Web Application**
A user-friendly web interface where users can:
- Input messages for real-time classification.
- View classification results for various disaster-related categories.
- Explore visual insights from the processed data.

#### Screenshot 1: Classification Results
![Classification Results](one.png)

#### Screenshot 2: Application Interface
![image](https://github.com/user-attachments/assets/a34c246d-1163-4a4c-81b8-3064f42891d6)


#### Screenshot 3: Message Category Distribution
![Message Category Distribution](two.png)

---

## **How to Use the Project**

1. **Environment Setup**: Install the required libraries and dependencies.  
2. **Data Preparation**: Use the ETL pipeline to clean and process the datasets into a structured format.  
3. **Model Training**: Train the machine learning model on the cleaned data and save the trained model for deployment.  
4. **Run the Web App**: Start the web application to classify messages and explore data visualizations.

---

## **Credits and Acknowledgments**
This project leverages real-world datasets and serves as a practical exercise in data engineering and machine learning. Special thanks to the dataset providers and educational platforms that made this work possible.

---

## **References**

- [stephanieirvine/Udacity-Data-Scientist-Nanodegree](https://github.com/stephanieirvine/Udacity-Data-Scientist-Nanodegree)
- [Sajjadmanal/Udacity-Data-Scientist-Nanodegree](https://github.com/Sajjadmanal/Udacity-Data-Scientist-Nanodegree)
- [Knowledge Portal](#)
- [YouTube Video: Disaster Response Pipeline Project](https://www.youtube.com/watch?v=wBNYrd1gQH0)
- [canaveensetia/udacity-disaster-response-pipeline](https://github.com/canaveensetia/udacity-disaster-response-pipeline)

**Articles:**
- [Udacity Data Scientist Nanodegree review, and whether it is worth the huge premium](#)
- [The Udacity Data Science Nanodegree — What do you actually learn about Data Science?](#)
- [Udacity Data Scientist Nanodegree Review](#)

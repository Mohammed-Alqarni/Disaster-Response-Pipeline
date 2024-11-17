# **Disaster Response Pipeline Project**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [File Descriptions](#file-descriptions)
3. [Installation Instructions](#installation-instructions)
4. [ETL Pipeline](#etl-pipeline)
5. [ML Pipeline](#ml-pipeline)
6. [Web Application](#web-application)
7. [Acknowledgments](#acknowledgments)

---

## **Project Overview**

This project demonstrates a pipeline for disaster response, utilizing data from real-world messages sent during disaster events. The system integrates an **ETL pipeline** to preprocess the data, an **ML pipeline** to build a machine learning model for multi-label classification, and a **web application** to interactively classify new messages.

Key objectives:
- Build an **ETL pipeline** to clean and save data into an SQLite database.
- Develop an **ML pipeline** to train a model that classifies messages into multiple categories.
- Provide a **web app** interface to classify messages and visualize data insights.

---

## **File Descriptions**

The repository contains the following essential files:

| File/Folder                  | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| `data/process_data.py`       | Script to clean data and save it into an SQLite database.     |
| `data/disaster_messages.csv` | Dataset containing messages sent during disaster events.      |
| `data/disaster_categories.csv` | Dataset with categories for each message.                 |
| `models/train_classifier.py` | Script to build, train, and save the ML model.               |
| `app/run.py`                 | Flask web application to classify messages interactively.    |
| `templates/*`                | HTML templates for the web app (e.g., `master.html`).        |
| `README.md`                  | Project documentation (this file).                           |

---

## **Installation Instructions**

### **Dependencies**
This project uses Python 3 and the following libraries:
- `pandas`
- `numpy`
- `sqlalchemy`
- `nltk`
- `scikit-learn`
- `flask`
- `plotly`
- `pickle`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## **ETL Pipeline**

The ETL pipeline processes disaster data and saves the cleaned results into a database.

### **Steps**
1. Load the data from `disaster_messages.csv` and `disaster_categories.csv`.
2. Merge datasets on the `id` column.
3. Clean the data:
   - Split `categories` into separate columns.
   - Convert category values into binary integers.
   - Remove duplicates and missing data.
4. Save the cleaned data into an SQLite database (`DisasterResponse.db`).

### **Run the ETL Pipeline**
```bash
python data/process_data.py \
'/path/to/disaster_messages.csv' \
'/path/to/disaster_categories.csv' \
'/path/to/DisasterResponse.db'
```

---

## **ML Pipeline**

The ML pipeline trains a machine learning model to classify messages into disaster-related categories.

### **Steps**
1. Load data from the SQLite database (`DisasterResponse.db`).
2. Split the data into training and test sets.
3. Build a machine learning pipeline:
   - Text preprocessing (TF-IDF and tokenization).
   - Multi-output classification using Random Forest.
4. Optimize the model using GridSearchCV.
5. Evaluate the model on test data using accuracy, F1-score, and precision.
6. Save the trained model as a pickle file (`classifier.pkl`).

### **Run the ML Pipeline**
```bash
python models/train_classifier.py \
'/path/to/DisasterResponse.db' \
'/path/to/classifier.pkl'
```

---

## **Web Application**

A Flask-based web application allows users to:
- Input new messages for classification.
- Visualize insights from the training dataset.

### **How to Run the App**
1. Run the Flask app:
   ```bash
   python app/run.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Results and Evaluation**

- **ETL Pipeline**: Successfully processes and cleans the dataset, saving it into an SQLite database.
- **ML Pipeline**:
  - Achieved an overall accuracy of ~95%.
  - Outputs multi-label classifications for each message.
  - Uses Random Forest as the classification model.
- **Web App**: Provides a user-friendly interface for real-time message classification.

---

## **Acknowledgments**

- **Data Source**: The datasets are provided by [Figure Eight](https://appen.com/).
- **Starter Code**: Special thanks to Udacity for the project starter code.
- **Libraries Used**: Python libraries such as `nltk`, `pandas`, `scikit-learn`, and `flask`.

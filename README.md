# 🤖 AI-Powered Business Recommendation System

An end-to-end Machine Learning project that recommends the most suitable digital services for businesses based on their industry, business size, digital presence, SEO score, marketing budget, and business goals.

This project was developed as part of the **Kalvix Nexus AI/ML Internship Assessment**.

## 📌 Project Overview

Businesses often struggle to identify which digital service best fits their needs.

This project uses Machine Learning to recommend services such as:

- Website Development
- SEO
- Branding
- Social Media Marketing
- App Development
- AI Automation

The recommendation is generated based on multiple business attributes and presented through a Streamlit web application.

## 🚀 Features

- Business Service Recommendation
- Data Cleaning & Preprocessing
- Feature Engineering
- Machine Learning Model Comparison
- Interactive Streamlit Web Application
- Model Evaluation
- Business-Friendly Predictions

## 📂 Dataset

The dataset contains **500 synthetic business records**.

### Features

- Business Name
- Industry
- Business Size
- Existing Website
- Social Media Presence
- SEO Score
- Marketing Budget
- Business Goal

### Target

- Recommended Service

## 🤖 Machine Learning Models

Two classification algorithms were implemented:

- Decision Tree Classifier
- Random Forest Classifier

After evaluation, the **Decision Tree Classifier** achieved the highest accuracy and was selected as the final model.

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Decision Tree | 98% |
| Random Forest | 90% |

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## 📁 Project Structure

AI_Business_Recommendation_System/

├── dataset/

│ ├── business_dataset.csv

│ └── business_dataset_processed.csv

├── models/

│ ├── business_recommendation_model.pkl

│ └── label_encoders.pkl

├── notebooks/

│ └── Business_Recommendation_System.ipynb

├── screenshots/

├── app.py

├── requirements.txt

├── README.md

└── report.pdf

## ⚙️ Installation

Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 📸 Screenshots - business_service_task\screenshots

## 🔮 Future Scope

- Explainable AI (SHAP)
- AI Chatbot Integration
- Cloud Deployment
- API Integration
- Deep Learning Models
- Real-time Business Analytics

## 👨‍💻 Author

Raj Kalavadiya

Flutter Developer | AI/ML Enthusiast

GitHub: YOUR_GITHUB

LinkedIn: YOUR_LINKEDIN
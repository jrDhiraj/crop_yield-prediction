🌾 Crop Yield Prediction using Machine Learning & Flask
📘 Overview

This project is a Crop Yield Prediction Web Application that uses Machine Learning to estimate crop yield based on key environmental and agricultural factors such as rainfall, temperature, and pesticide usage.
The model is trained on real agricultural data and deployed using Flask, allowing users to interact through a simple web interface.

🚀 Features

Predicts crop yield (hg/ha_yield) based on user input

Clean and responsive web UI built with HTML & CSS

Flask-based backend for serving real-time model predictions

Supports multiple crops and countries

Includes data preprocessing, encoding, and scaling pipeline

🧠 Machine Learning Workflow

Data Preprocessing

Removed duplicates and missing values

Handled non-numeric values in rainfall and temperature columns

Encoded categorical features using OneHotEncoder

Scaled numerical features with StandardScaler

Model Training

Trained multiple models:

Linear Regression

Ridge & Lasso

Decision Tree Regressor

Random Forest Regressor

Evaluated models using R² Score, MSE, and MAE

Selected Decision Tree Regressor as the final model

Model Deployment

Saved the trained model and preprocessor using pickle

Built a Flask app to load and predict using the saved model

Designed a frontend for user input and output display

⚙️ Tech Stack
Component	Technology
Language	Python
Libraries	NumPy, Pandas, scikit-learn, Seaborn, Matplotlib
Backend	Flask
Frontend	HTML, CSS
IDE	VS Code

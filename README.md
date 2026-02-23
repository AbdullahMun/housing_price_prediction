# 🏠 California Housing Price Prediction - Machine Learning Project

## Project Overview

This project was developed as part of the Machine Learning Internship (Month 2 Task 3).  
The main objective is to build a Machine Learning model that predicts house prices based on important features such as:

- Location (latitude and longitude)
- Number of rooms
- Population
- Income and other housing-related attributes

The trained model is deployed using Streamlit to create an interactive web application where users can enter house details and receive real-time price predictions along with visual insights.



## Project Objectives

The goals of this project are:

- Perform data preprocessing and cleaning
- Explore and visualize housing data
- Train a machine learning regression model
- Evaluate model performance
- Deploy the model using Streamlit
- Create an interactive prediction dashboard



## Dataset

The California Housing dataset was downloaded from Kaggle and stored locally to avoid runtime internet dependency.

### Dataset Features

- longitude → geographical location
- latitude → geographical location
- housing_median_age → age of house
- total_rooms → total number of rooms
- total_bedrooms → total bedrooms
- population → population of area
- households → number of households
- median_income → income level
- median_house_value → target variable (house price)



## Data Preprocessing

The following preprocessing steps were applied:

- Loaded dataset from local CSV file
- Removed categorical column (`ocean_proximity`) for simplicity
- Renamed target column to `HousePrice`
- Handled missing values using mean imputation
- Checked correlations between features


## Data Visualization

Several visualizations were created to understand data patterns:

- Correlation Heatmap
- House Price Distribution
- Scatter Plot (Income vs Price)

Dynamic visualization added:

- Predicted Price vs Dataset Average comparison
- Live map showing selected house location


## Machine Learning Model

### Algorithm Used:

Linear Regression

### Steps:

1. Feature selection
2. Train-test split (80% training, 20% testing)
3. Model training
4. Prediction on test data
5. Performance evaluation


## Model Evaluation

Since this is a regression problem, accuracy is not used.

Instead, the following metrics were applied:

- Mean Absolute Error (MAE)
- R² Score (Coefficient of Determination)

These metrics help measure how close the predicted values are to actual house prices.



## Streamlit Web Application

The trained model was deployed using Streamlit.

### Features:

- User input panel (sidebar)
- Real-time house price prediction
- Data visualization dashboard
- Dynamic graphs based on prediction
- Interactive map showing selected location


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit


## Project Structure

Project Task 3/ │ ├── app.py ├── housing_price_prediction.ipynb ├── housing_model.pkl ├── housing.csv ├── requirements.txt ├── README.md



## How to Run the Project

### Step 1 — Create Virtual Environment
python -m venv venv

### Step 2 — Activate Environment
venv\Scripts\activate

### Step 3 — Install Dependencies
pip install -r requirements.txt

### Step 4 — Run Streamlit App
streamlit run app.py


## Key Learning Outcomes

- Understanding regression-based machine learning
- Data preprocessing and handling missing values
- Model training and evaluation
- Data visualization techniques
- Building interactive dashboards with Streamlit
- Deploying ML models into real-world applications

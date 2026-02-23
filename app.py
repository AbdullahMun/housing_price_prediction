import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Housing Price Prediction", layout="wide")

st.title("🏠 California Housing Price Prediction Dashboard")

# Load Model and Dataset

model = joblib.load("housing_model.pkl")
df = pd.read_csv("housing.csv")

# Drop categorical column if exists
if "ocean_proximity" in df.columns:
    df = df.drop("ocean_proximity", axis=1)

if "median_house_value" in df.columns:
    df.rename(columns={"median_house_value": "HousePrice"}, inplace=True)

# Sidebar Inputs

st.sidebar.header("Enter House Details")

input_data = []

for column in df.columns:
    if column != "HousePrice":
        value = st.sidebar.number_input(f"{column}", float(df[column].mean()))
        input_data.append(value)


# Prediction + Visualization Section

if st.sidebar.button("Predict Price"):
    
    # Convert input into numpy array
    features = np.array([input_data])
    
    # Make prediction
    prediction = model.predict(features)
    
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")

    # Dynamic Graph 1: Predicted vs Average Price
    
    avg_price = df["HousePrice"].mean()

    st.write("### 📊 Predicted Price vs Dataset Average")

    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(["Average Price", "Your Predicted Price"],
               [avg_price, prediction[0]])
    ax_bar.set_ylabel("Price")
    st.pyplot(fig_bar)


    # Dynamic Graph 2: Location Map-

    st.write("### 📍 Selected House Location")

    location_df = pd.DataFrame({
        "lat": [input_data[df.columns.get_loc("latitude")]],
        "lon": [input_data[df.columns.get_loc("longitude")]]
    })

    st.map(location_df)

    
    # Show Visualizations
    
    st.subheader("📊 Data Visualizations")

    col1, col2 = st.columns(2)

    # Correlation Heatmap
    with col1:
        st.write("### Correlation Heatmap")
        fig1, ax1 = plt.subplots()
        sns.heatmap(df.corr(), cmap="coolwarm", ax=ax1)
        st.pyplot(fig1)

    # Distribution Plot
    with col2:
        st.write("### House Price Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(df["HousePrice"], bins=30, kde=True, ax=ax2)
        st.pyplot(fig2)

    # Scatter Plot
    st.write("### Income vs House Price")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(x=df.iloc[:,0], y=df["HousePrice"], ax=ax3)
    st.pyplot(fig3)


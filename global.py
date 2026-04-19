import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# load data
df = pd.read_csv("g.csv")

# features and target
X = df[['year', 'co2']]
y = df['temperature_anomaly']

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# train model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# evaluate
y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)

# UI
st.title("🌍 Global Warming Prediction App")
st.write(f"Model R² Score: {r2:.2f}")

year = st.number_input("Enter Year", value=2030)
co2 = st.number_input("Enter CO₂ level (ppm)", value=430)

if st.button("Predict"):
    user_data = scaler.transform([[year, co2]])
    prediction = model.predict(user_data)

    st.success(f"Predicted Temperature Anomaly: {prediction[0]:.2f} °C")
    
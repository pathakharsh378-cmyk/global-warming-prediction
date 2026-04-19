# global-warming-prediction
# 🌍 Global Warming Prediction using Machine Learning

## 📌 Project Overview

This project predicts **global temperature rise (temperature anomaly)** using Machine Learning based on:

* Year
* CO₂ (carbon dioxide levels)

The model learns the relationship between increasing CO₂ levels and global warming trends.

---

## 🚀 Features

* Predict temperature anomaly based on user input
* Interactive web app using Streamlit
* Data visualization of climate trends
* Simple and clean ML pipeline

---

## 🧠 Machine Learning Model

* Model Used: Linear Regression
* Features: `year`, `co2`
* Target: `temperature_anomaly`
* Evaluation Metric: R² Score

---

## 📊 Dataset

* Based on global climate trends from NASA
* Includes:

  * Year (1950–2025)
  * CO₂ levels (ppm)
  * Temperature anomaly (°C)

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/global-warming-ml.git
cd global-warming-ml
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the app

```
streamlit run global.py
```

---

## 💻 Usage

1. Enter **Year**
2. Enter **CO₂ level (ppm)**
3. Click **Predict**
4. Get predicted temperature anomaly

---

## 📈 Example

Input:

* Year: 2030
* CO₂: 430

Output:

* Predicted Temperature Anomaly: ~1.3°C

---

## 📷 Screenshots

(Add screenshots of your app here)

---

## 📌 Future Improvements

* Use advanced models (Random Forest, LSTM)
* Add real-time climate data API
* Improve UI/UX
* Add global map visualization

---

## 👨‍💻 Author

Harsh Pathak

---

## 📜 Note

This project uses simplified climate data for learning purposes.
It does not represent exact scientific predictions.

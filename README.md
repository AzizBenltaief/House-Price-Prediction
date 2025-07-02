# 🏡 Bangalore House Price Prediction

A web application that predicts housing prices in Bangalore based on area (sqft), 
number of bedrooms (BHK), number of bathrooms, and location.

---

## 🚀 Features

- Predicts house prices using a trained machine learning model.
- Interactive web interface using HTML, CSS, and JavaScript.
- Backend powered by Flask.
- Location list dynamically fetched from the backend.
- Trained model and metadata stored in `.pickle` and `.json` files.

---

## 🧠 Tech Stack

| Frontend     | Backend     | ML Model         | Other            |
|--------------|-------------|------------------|------------------|
| HTML, CSS, JS| Python Flask| scikit-learn     | NumPy, Pandas    |

---

## 📂 Project Structure

HousePricePrediction/
│
├── artifacts/ # Contains trained model and columns
│ ├── banglore_home_prices_model.pickle
│ └── columns.json
│
├── server/
│ ├── server.py # Flask backend
│ └── util.py # Helper functions for prediction
│
├── static/
│ ├── app.css # Styles
│ └── app.js # JavaScript logic
│
├── templates/
│ └── index.html # Frontend page

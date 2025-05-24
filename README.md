
# 🌾 Crop Prediction using Machine Learning

This project predicts the most suitable crop to grow based on environmental parameters such as temperature, humidity, soil pH, and rainfall using a machine learning model.

---

## 🚀 Project Overview

With increasing demand for efficient agriculture, predicting the best crop based on environmental conditions can help farmers make informed decisions. This project uses a **Random Forest Classifier** trained on a labeled dataset to predict crops with high accuracy.

---

## 📁 Dataset

The dataset `cpdata.csv` contains:

| Feature      | Description                        |
|--------------|------------------------------------|
| temperature  | Average temperature (°C)           |
| humidity     | Relative humidity (%)              |
| ph           | Soil pH level                      |
| rainfall     | Annual rainfall (mm)               |
| label        | Crop name (Target variable)        |

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- Jupyter Notebook / Python Script

---

## 📦 Required Libraries

Install the dependencies using pip:

```bash
pip install pandas scikit-learn

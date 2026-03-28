# 📰 Fake News Detection Web App using NLP

A Machine Learning based web application that detects whether a news article is **REAL** or **FAKE** using Natural Language Processing (NLP) techniques and a Streamlit user interface.

---

## 🚀 Project Overview

This project builds a text classification model trained on real-world news data.
Users can input any news content, and the system predicts whether the news is fake or real in real-time.

---

## ✨ Features

* 🔍 Fake vs Real news classification
* ⚡ Real-time prediction using Streamlit UI
* 🧠 NLP preprocessing with TF-IDF Vectorization
* 📊 High accuracy (~99%)
* 💾 Model persistence using Pickle
* 🖥️ Simple and interactive web interface

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* NLP (TF-IDF Vectorizer)

---

## 📂 Project Structure

```
fake-news-detection
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
```

---

## 📊 Dataset

The model is trained on the Fake News Dataset available on Kaggle:

Dataset Link:
https://www.kaggle.com/datasets/abaghyangor/fake-news-dataset

Download the dataset and place the CSV files in your project directory before training.

---

## ⚙️ Installation

### Step 1 — Clone Repository

```
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### Step 2 — Install Dependencies

```
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run the training script to generate model files:

```
python train.py
```

This will create:

* fake_news_model.pkl
* tfidf_vectorizer.pkl

---

## ▶️ Run Streamlit App

```
streamlit run app.py
```

App will open in your browser.

---

## 🖥️ Application UI

* Enter news text
* Click **Check News**
* Model predicts REAL or FAKE

---

## 📈 Model Details

* Algorithm: LinearSVC / Logistic Regression
* Vectorization: TF-IDF
* Train/Test Split: 80/20
* Accuracy: ~99%

---

## 🔮 Future Improvements

* Upload news article file
* Add news URL detection
* Deploy on Streamlit Cloud
* Add deep learning model (LSTM/BERT)

---

## 👤 Author

Prince 
Connect me on Linkedin : www.linkedin.com/in/prince-hub716/


---

## ⭐ If you like this project

Give it a star on GitHub ⭐

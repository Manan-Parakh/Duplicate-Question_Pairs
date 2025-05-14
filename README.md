# Quora Duplicate Question Pair App

[🚀 Streamlit App](https://duplicate-questions-pair-checker.streamlit.app/)

This project tackles the Quora Question Pairs challenge, where the objective is to determine whether two given questions are semantically similar or duplicates. It combines data science, natural language processing, and machine learning, and is deployed via Streamlit for real-time inference.

---

## 🚀 What I Did

This project was initially developed in a Jupyter Notebook and later deployed using **Streamlit**. It follows a full end-to-end data science pipeline:

### 📦 1. Setup

* Downloaded the dataset using the Kaggle API.
* Loaded and explored the data to understand its structure and content.

### 📊 2. Exploratory Data Analysis (EDA)

* Analyzed the distribution of classes (`is_duplicate`).
* Checked for missing values.
* Gained insights into the dataset with basic statistics and visualizations.

### 🧹 3. Preprocessing

* Lowercased all text.
* Removed punctuation and stopwords.
* Replaced special symbols with corresponding text (e.g., `$` → *dollar*).
* Expanded contractions (e.g., *isn't* → *is not*).

### 🧠 4. Feature Engineering

Developed a range of handcrafted features to enhance model performance:

#### ✔️ Basic Features

* Length-based metrics such as word count, character count, and length differences.

#### ✔️ Advanced Features

* **Token Features**:

  * `cwc_min`, `cwc_max`: Common word count ratios.
  * `csc_min`, `csc_max`: Common stopword count ratios.
  * `ctc_min`, `ctc_max`: Common token count ratios.
* **Fuzzy Features**:

  * Fuzzy string similarity scores using the FuzzyWuzzy library.

### 🧰 5. Vectorization

* Transformed text using **Bag-of-Words (BoW)** vectorizer to convert raw questions into numerical form for modeling.

### 🤖 6. Modeling

* Trained and evaluated the following classifiers:

  * Random Forest Classifier
  * XGBoost Classifier

* Used metrics like accuracy, precision, recall, F1-score, and confusion matrices for performance evaluation.

### 🧪 7. Performance Comparison

* Compared models with and without advanced feature engineering.
* Visualized ROC curves and confusion matrices to analyze model performance.

---

## 💡 Project Highlights

* Complete ML pipeline for semantic text classification.
* Rich feature engineering to capture nuanced question similarity.
* Clean modular deployment via Streamlit for user interaction.
* Reproducible in Google Colab or Jupyter Notebook.

---

## 📁 Deployment Architecture

The deployment is organized into two modular files:

* `app.py`: Main application logic and user interface using Streamlit.
* `helper.py`: Contains all preprocessing functions, feature extraction methods, and model loading utilities.

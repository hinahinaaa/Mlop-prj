# 🏡 House Price Prediction - MLOps Project

This project is a **House Price Prediction** task using **XGBoost**. The goal is to predict house prices based on various features. The project demonstrates an **end-to-end MLOps pipeline** including data preparation, model training, evaluation, and experiment tracking.

## 📊 Project Overview

The goal of this project is to build a predictive model that estimates **SalePrice** of houses based on 79 features including square footage, neighborhood, garage capacity, etc. We use **XGBoost Regressor**, a powerful gradient boosting machine learning algorithm, for model training and evaluation.

### Key Steps:
![MLOps Pipeline](https://i.imgur.com/YasAOB0.png)
---

This pipeline includes the following stages:

1. **Input data** - Load the raw dataset from Kaggle.
2. **EDA** - Explore the dataset to understand structure, patterns, and correlations.
3. **Features selection** - Select important features based on EDA insights.
4. **Preprocess** - Handle missing values, encode categorical features, and scale numerical values.
5. **Train and evaluate the performance of multiple model** - Train various models including XGBoost Regressor and evaluate using R², MAE, RMSE.
6. **FastAPI** - Develop an API endpoint for serving the model.
7. **Weights & Biases** - Track experiments, visualize training metrics, and manage model versions.

---

## 🛠️ Technologies & Tools Used

- **Python** (3.x)
- **XGBoost**: Gradient Boosting Machine for regression tasks
- **pandas** & **numpy**: Data manipulation and numerical operations
- **matplotlib** & **seaborn**: Data visualization
- **scikit-learn**: For preprocessing, splitting data, and model evaluation
- **wandb**: Weights and Biases for experiment tracking and model logging
- **Jupyter Notebooks**: Interactive coding environment for exploration and experimentation

## 📂 Folder Structure

```

Mlop-prj/
│
├── 1\_fetch\_data.ipynb               # Load and prepare the raw dataset
├── 2\_eda.ipynb                      # Exploratory Data Analysis (EDA)
├── 3\_preprocessing.ipynb           # Data cleaning, encoding, and scaling
├── 4\_train\_test.ipynb              # Training and evaluating the model
│
├── house-prices-advanced-regression-techniques.zip # Dataset file
├── requirements.txt                # List of dependencies
│
├── artifacts/                      # Model artifacts and outputs
└── wandb/                          # Weights and Biases logs

````

## 📈 Dataset Overview

The dataset used in this project is the **"House Prices: Advanced Regression Techniques"** dataset from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques). It consists of 79 features and the target variable is **SalePrice**, the final price of the house.

Key features:
- **GrLivArea**: Above grade (ground) living area in square feet
- **GarageCars**: Size of garage in car capacity
- **YearBuilt**: Year the house was built
- **OverallQual**: General quality of the house
- **Neighborhood**: Location where the house is situated

## ⚙️ Installation & Setup

### Prerequisites:
- Python 3.x
- Virtual environment (recommended)

### Steps to Install:
1. Clone the repository:

```bash
git clone https://github.com/I-KUN-I/Mlop-prj.git
cd Mlop-prj
````

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Launch Jupyter notebook:

```bash
jupyter notebook
```

## 🔍 Workflow

### Step 1: **Data Acquisition**

* Download and unzip the dataset from Kaggle.

### Step 2: **Exploratory Data Analysis (EDA)**

* Investigate the dataset, visualize the distribution of target variable `SalePrice`, and check for any patterns or outliers.

### Step 3: **Preprocessing**

* Handle missing data, encode categorical features, and scale numerical data.

### Step 4: **Model Training with XGBoost**

* Train a **XGBoost Regressor** model to predict house prices.

### Step 5: **Model Evaluation**

* Evaluate the model using metrics like **R² Score**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.
* Visualize the results and compare predicted vs. actual values.

## 🧠 Model Used

### **XGBoost Regressor**

XGBoost is an advanced gradient boosting algorithm known for its performance and speed. It builds an ensemble of decision trees and uses boosting to improve accuracy by learning from previous trees' errors.

Key features of XGBoost:

* **Boosting**: Sequentially builds models to correct the errors of the previous one.
* **Regularization**: Helps prevent overfitting through L1 and L2 regularization.
* **Handling Missing Data**: XGBoost can handle missing values efficiently.
* **Feature Importance**: Provides insights into which features contribute most to the model's predictions.

## 📈 Experiment Tracking with W\&B

This project uses **Weights & Biases (W\&B)** to track experiments and monitor model training. W\&B logs the metrics such as **R²**, **MAE**, and **RMSE** for each run, as well as other parameters like **learning rate** and **number of trees**.

* **Install W\&B**:

```bash
pip install wandb
```

* **Login to W\&B**:

```bash
wandb login
```

* **Track the experiment**:

```python
import wandb
wandb.init(project="house-price-prediction")

# Log metrics
wandb.log({"r2_score": r2_score})
```

## 🏆 Model Evaluation

After training the model, we evaluate it using the following metrics:

* **R² Score**: Measures the proportion of the variance in the target variable that is predictable from the features.
* **Mean Absolute Error (MAE)**: The average of the absolute differences between predicted and actual values.
* **Root Mean Squared Error (RMSE)**: Measures the magnitude of the prediction error, with greater penalties for larger errors.

## 🚀 Future Enhancements

* **Hyperparameter Optimization**: Use GridSearchCV or RandomizedSearchCV for hyperparameter tuning.
* **Cross-validation**: Implement k-fold cross-validation to reduce overfitting and improve model performance.
* **Model Deployment**: Deploy the trained model using **Flask** or another web framework for real-time predictions.
* **Model Interpretability**: Use SHAP or LIME for model interpretation and better understanding of feature importance.

## 🤝 Contributing

Feel free to fork the repository and contribute by:

* Improving model accuracy
* Refactoring code
* Updating documentation
* Fixing bugs

## ⭐ Support the Project

If you found this project useful, please give it a ⭐ on GitHub! It helps the project reach a wider audience.

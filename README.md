# 🎓 Student Performance Predictor

A machine learning web application that predicts students' exam scores based on academic, personal, and environmental factors.

Built using **Python, Scikit-learn, Pandas, and Streamlit**.

## 🌐 Live Demo

Try the deployed Student Performance Predictor here:

🔗 [Launch Student Performance Predictor](https://mustabyte-student-performance-predictor.streamlit.app/)

## Project Overview

This project uses regression-based machine learning to predict a student's exam score from 19 input features, including study hours, attendance, previous scores, motivation, access to resources, and other factors.

The project covers the complete machine learning workflow, from data exploration and preprocessing to model comparison, evaluation, and web application development.

## Dataset

**Student Performance Factors**

The dataset contains information about student performance and factors potentially associated with exam scores.

- Original records: 6,607
- Records after cleaning: 6,606
- Input features: 19
- Target variable: `Exam_Score`

## Machine Learning Workflow

1. Data loading and exploration
2. Data cleaning and validation
3. Exploratory data analysis (EDA)
4. Feature selection and target definition
5. Train-test splitting
6. Missing-value imputation and one-hot encoding
7. Baseline model training and evaluation
8. Model comparison
9. Five-fold cross-validation
10. Hyperparameter tuning
11. Final model selection
12. Model serialization and Streamlit integration

## Models Evaluated

Four regression algorithms were evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

The tree-based models were additionally evaluated using hyperparameter tuning.

### Final Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| **Linear Regression** | **0.42** | **1.52** | **0.8250** |
| Tuned Decision Tree | 1.52 | 2.51 | 0.5248 |
| Tuned Random Forest | 1.03 | 1.91 | 0.7233 |
| Tuned Gradient Boosting | 0.63 | 1.62 | 0.8025 |

**Linear Regression** was selected as the final model based on its evaluation results and cross-validation performance.

## Preprocessing Pipeline

The saved machine learning pipeline includes:

- Median imputation for numerical features
- Most-frequent imputation for categorical features
- One-hot encoding for categorical variables
- Linear Regression for exam score prediction

Preprocessing is fitted using training data to avoid data leakage.

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

## Project Structure

```text
student-performance-predictor/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── StudentPerformanceFactors.csv
├── model/
│   └── student_model.pkl
└── notebooks/
    └── student_model.ipynb
```

## Run Locally

Clone the repository and navigate into the project directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app.py
```

## Limitations

- Predictions are estimates, not guaranteed exam results.
- Rare high-scoring students may be significantly underpredicted.
- The model was trained on one dataset and may not generalize to other student populations.
- The application is intended for educational demonstration.

## Future Improvements

- Additional datasets and external validation
- Model interpretability and feature importance analysis
- Improved predictions for unusual student profiles
- Enhanced Streamlit interface and visualizations

## Author

Mustab Shera Binte Junayed

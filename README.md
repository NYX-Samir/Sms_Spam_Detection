
# SMS Spam Detection

A comprehensive machine learning project to classify SMS messages as spam or ham using various classification algorithms and NLP techniques.

## Project Overview

This project implements a robust SMS spam detection system that processes text messages and classifies them as either spam or legitimate messages. The system compares multiple machine learning algorithms to find the most effective approach for spam detection.

## Features

- **Data Preprocessing**: Text cleaning, tokenization, stopword removal
- **Multiple Algorithms**: Comparison of 8+ classification models
- **Performance Metrics**: Accuracy, precision, recall, and F1-score
- **Visualization**: Detailed plots and model comparisons
- **Feature Engineering**: TF-IDF and Count Vectorizer

## Dataset

Uses the SMS Spam Collection dataset from Kaggle containing:
- 5,572 SMS messages
- Labeled as "spam" or "ham" (legitimate)
- 4,827 ham messages (86.6%)
- 747 spam messages (13.4%)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/NYX-Samir/Sms_Spam_Detection.git
cd Sms_Spam_Detection
```

2. **Install dependencies**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn nltk jupyter wordcloud xgboost
```

## Usage

1. **Start Jupyter Notebook**:
```bash
jupyter notebook
```

2. **Open the main notebook**:
   - Navigate to `notebook/Spam detection .ipynb`
   - Run all cells sequentially

## Models Implemented

- Naive Bayes (Multinomial & Bernoulli)
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- K-Nearest Neighbors (KNN)
- Decision Tree
- Gradient Boosting
- XGBoost

## Project Structure

```
Sms_Spam_Detection/
├── notebook/
│   └── Spam detection .ipynb    # Main Jupyter notebook
├── data/                        # Dataset directory
├── models/                      # Trained models
├── results/                     # Output and visualizations
└── README.md
```

## Results

The project provides comprehensive performance comparisons including:
- Accuracy scores for all models
- Precision, recall, and F1-score metrics
- Confusion matrices
- ROC curves and AUC scores
- Feature importance analysis

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available under the MIT License.

## Author

**Samir NYX**
- GitHub: [@NYX-Samir](https://github.com/NYX-Samir)
```

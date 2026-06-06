# Email/SMS Spam Classifier

A machine learning-based application that classifies emails and SMS messages as spam or legitimate using a trained Naive Bayes model with TF-IDF vectorization.

## 📋 Project Overview

This project implements a spam classification system using:
- **Machine Learning Model**: Naive Bayes classifier
- **Text Processing**: TF-IDF vectorization with preprocessing (tokenization, stemming, stopword removal)
- **Web Interface**: Streamlit for easy deployment and user interaction
- **Training Data**: Kaggle spam dataset with 5,572 messages

## 🏗️ Project Structure

```
Email Classifier/
│
├── src/                          # Source code
│   └── app.py                   # Streamlit web application
│
├── data/
│   ├── raw/                     # Raw datasets
│   │   └── spam.csv            # Original training dataset
│   └── models/                  # Trained model files
│       ├── model.pkl           # Trained Naive Bayes model
│       └── vectorizer.pkl      # TF-IDF vectorizer
│
├── notebooks/                   # Jupyter notebooks
│   └── email_classifier.ipynb  # Model training and analysis notebook
│
├── docs/                        # Documentation
│   └── (placeholder for additional docs)
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore file
└── setup.py                     # Optional: Package setup file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip or conda package manager
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd "Email Classifier"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Running the Streamlit App

```bash
streamlit run src/app.py
```

The application will open in your default browser at `http://localhost:8501`

**How to use:**
1. Enter your email or SMS message in the text area
2. Click the "Predict" button
3. The app will display whether the message is "Spam" or "Not spam"

### Training/Experimenting with the Model

Open the Jupyter notebook to see the complete model training pipeline:

```bash
jupyter notebook notebooks/email_classifier.ipynb
```

## � Screenshots

### Application Interface
![Screenshot 1](outputs/screenshot1.png)
*Email Classifier Streamlit interface*

![Screenshot 2](outputs/screenshot2.png)
*Prediction output example*

## �🔧 Dependencies

All required packages are listed in `requirements.txt`:

- **streamlit**: Web application framework
- **nltk**: Natural Language Toolkit for text preprocessing
- **scikit-learn (sklearn)**: Machine learning library

These packages include:
- pandas, numpy (data manipulation)
- Any other dependencies required by the above packages

## 📊 Model Details

### Model Architecture
- **Algorithm**: Naive Bayes Classifier
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Training Data**: 5,572 messages (spam and legitimate)

### Text Preprocessing Pipeline
1. **Lowercasing**: Convert text to lowercase
2. **Tokenization**: Split text into individual words
3. **Removing Non-alphanumeric**: Filter special characters
4. **Stopword Removal**: Remove common English words
5. **Stemming**: Reduce words to their root form (Porter Stemmer)

### Files
- `data/models/model.pkl`: Trained Naive Bayes model
- `data/models/vectorizer.pkl`: Fitted TF-IDF vectorizer

## 📁 Data

- **Location**: `data/raw/spam.csv`
- **Format**: CSV file with email/SMS messages and labels
- **Target**: Binary classification (spam = 1, legitimate = 0)

## 🐳 Deployment

### Local Deployment
```bash
streamlit run src/app.py
```

### Docker Deployment (Optional)

Create a `Dockerfile` in the root directory:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py"]
```

Build and run:
```bash
docker build -t spam-classifier .
docker run -p 8501:8501 spam-classifier
```

### Cloud Deployment

**Streamlit Cloud** (Recommended for quick deployment):
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "Deploy an app" and select your repository
4. Configure the settings and deploy

**Heroku, AWS, Google Cloud, Azure**: Similar deployment procedures available.

## 📈 Performance Metrics

You can check the model's performance metrics in the Jupyter notebook. Common metrics include:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🛠️ Development

### Project Workflow

1. **Data Preparation** (in notebook):
   - Load and explore `spam.csv`
   - Clean and preprocess data
   - Split into train/test sets

2. **Model Training** (in notebook):
   - Vectorize text using TF-IDF
   - Train Naive Bayes classifier
   - Evaluate performance

3. **Model Serialization**:
   - Save trained model to `model.pkl`
   - Save vectorizer to `vectorizer.pkl`

4. **Deployment**:
   - Use `app.py` for Streamlit deployment

### Making Changes

To retrain the model:
1. Update `data/raw/spam.csv` with new data if needed
2. Run the Jupyter notebook to train
3. The new `model.pkl` and `vectorizer.pkl` will be saved
4. Restart the Streamlit app

## 📝 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| NLTK data not found | The app automatically downloads required NLTK data on first run |
| Model files not found | Ensure `data/models/` contains `model.pkl` and `vectorizer.pkl` |
| Port 8501 already in use | Use `streamlit run src/app.py --server.port 8502` |
| Import errors | Run `pip install -r requirements.txt` again |

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [NLTK Documentation](https://www.nltk.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

Created as a machine learning project for email/SMS spam classification.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📧 Feedback & Support

For issues or suggestions, please open an issue in the repository.

---

**Last Updated**: June 2026
**Version**: 1.0

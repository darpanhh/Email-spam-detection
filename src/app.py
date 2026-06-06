import streamlit as st
import pickle
import string
import os
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Get the directory of the app file and construct paths to model files
app_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(app_dir, '..', 'data', 'models')

tfidf = pickle.load(open(os.path.join(model_dir, 'vectorizer.pkl'), 'rb'))
model = pickle.load(open(os.path.join(model_dir, 'model.pkl'), 'rb'))

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message:")

if st.button('Predict'):
    
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms]).toarray()
    result = model.predict(vector_input)[0]

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not spam')

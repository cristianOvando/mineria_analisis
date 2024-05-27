import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

data = pd.read_csv('Cleaned_TaskMaster.csv')

if 'Unnamed: 0' in data.columns:
    data = data.drop(columns=['Unnamed: 0'])

lemmatizer = WordNetLemmatizer()

def apply_lemmatization(text):
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmas)

text_columns = data.select_dtypes(include=['object']).columns
for col in text_columns:
    data[col] = data[col].apply(apply_lemmatization)

data.to_csv('Lemmatized_TaskMaster.csv', index=False)

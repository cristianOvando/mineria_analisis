import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

data = pd.read_csv('Cleaned_Respuestas.csv')

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

data['Si tuvieras una aplicación para registrar todas tus actividades, ¿para qué ámbitos la usarías?'] = \
    data['Si tuvieras una aplicación para registrar todas tus actividades, ¿para qué ámbitos la usarías?'].replace(
        ['Todas mis actividades cotidianas', 'Para todo ambito'], 
        'Para todo ambito'
    )

data['¿En cual de las siguientes opciones prefieres anotar tus actividades?'] = \
    data['¿En cual de las siguientes opciones prefieres anotar tus actividades?'].replace(
        'Programas que utilizan la sincronización de datos tanto en el teléfono como en el programa de escritorio', 
        'Programa para celular'
    )

def update_color(row):
    if row == 'gris si no se a iniciado y rojo si no fue hecha':
        color_counts = data['¿Con qué color asocias más que una tarea está sin iniciar o no fue hecha?'].value_counts()
        most_common_color = color_counts.idxmax()
        return most_common_color
    return row

data['¿Con qué color asocias más que una tarea está sin iniciar o no fue hecha?'] = \
    data['¿Con qué color asocias más que una tarea está sin iniciar o no fue hecha?'].apply(update_color)

data.to_csv('Lemmatized_TaskMaster.csv', index=False)

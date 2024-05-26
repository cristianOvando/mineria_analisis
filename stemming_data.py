import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Asegúrate de tener descargados estos recursos
nltk.download('wordnet')
nltk.download('punkt')

# Cargar tu archivo CSV
data = pd.read_csv('Cleaned_TaskMaster.csv')

# Si el archivo tiene una columna sin nombre (usualmente de índices antiguos), la eliminamos
if 'Unnamed: 0' in data.columns:
    data = data.drop(columns=['Unnamed: 0'])

# Inicializar el lematizador
lemmatizer = WordNetLemmatizer()

# Función para aplicar la lematización a una oración
def apply_lemmatization(text):
    tokens = word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmas)

# Aplicar la lematización a todas las columnas de texto
text_columns = data.select_dtypes(include=['object']).columns
for col in text_columns:
    data[col] = data[col].apply(apply_lemmatization)

# Guardar los datos lematizados
data.to_csv('Lemmatized_TaskMaster.csv', index=False)

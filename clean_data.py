import pandas as pd

# Leer el archivo Excel en lugar de CSV
file_path = r'C:/Users/ovand/OneDrive/Documentos/Mineria/mineria_analisis/Respuestas.xlsx'
data = pd.read_excel(file_path)

# Eliminar la primera columna (si no es necesaria)
data_clean = data.drop(columns=[data.columns[0]])

# Función para convertir el texto a 'sentence case'
def to_sentence_case(text):
    return text.capitalize()

# Aplicar sentence case a todas las columnas de texto
text_columns = data_clean.select_dtypes(include=['object']).columns
for col in text_columns:
    data_clean[col] = data_clean[col].apply(to_sentence_case)

valid_devices = ['Android', 'ios']

data_clean['¿Qué sistema operativo utilizas?'] = data_clean['¿Qué dispositivo celular utilizas?'].apply(
    lambda x: x if x in valid_devices else None
)

data_clean = data_clean.dropna()

clean_file_path = 'Cleaned_Respuestas.xlsx'
data_clean.to_csv(clean_file_path, index=False)

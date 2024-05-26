import pandas as pd

file_path = 'TaskMaster.csv'
data = pd.read_csv(file_path)

data_clean = data.drop(columns=[data.columns[0]])

def to_sentence_case(text):
    return text.capitalize()

text_columns = data_clean.select_dtypes(include=['object']).columns
for col in text_columns:
    data_clean[col] = data_clean[col].apply(to_sentence_case)

data_clean['¿Cuántos años tienes?'] = data_clean['¿Cuántos años tienes?'].apply(lambda x: x if 0 < x < 120 else None)

data_clean = data_clean.dropna()

clean_file_path = 'Cleaned_TaskMaster.csv'
data_clean.to_csv(clean_file_path, index=False)

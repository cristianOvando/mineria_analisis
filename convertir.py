import pandas as pd

# Cargar el archivo Excel
file_path_xlsx = r'C:\Users\ovand\OneDrive\Documentos\Mineria\mineria_analisis\Respuestas.xlsx'
data = pd.read_excel(file_path_xlsx)

# Guardar el archivo como CSV
data.to_csv(r'C:\Users\ovand\OneDrive\Documentos\Mineria\mineria_analisis\Respuestas.csv', index=False)

print("Archivo convertido a CSV con éxito")

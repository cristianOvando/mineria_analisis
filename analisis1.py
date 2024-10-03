import pandas as pd
from ydata_profiling import ProfileReport

data = pd.read_excel(r'C:\Users\ovand\OneDrive\Documentos\Mineria\mineria_analisis\Respuestas.xlsx')

profile = ProfileReport(data, title='Análisis exploratorio', explorative=True)

profile.to_file("informe_optime.html")

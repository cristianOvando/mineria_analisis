import pandas as pd
from ydata_profiling import ProfileReport

data = pd.read_csv('Lemmatized_TaskMaster.csv')

profile = ProfileReport(data, title='Perfilado de Datos', minimal=True)

profile.to_file("analsis exploratorio.html")

import pandas as pd
from pandas_profiling import ProfileReport

file_path = 'Lemmatized_TaskMaster.csv'
data = pd.read_csv(file_path)

profile = ProfileReport(data, title='Analisis exploratorio', explorative=True)

profile.to_file("informe1_taskMaster.html")

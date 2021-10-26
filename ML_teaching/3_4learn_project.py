import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

work_dir = Path.cwd()
user_data_path = work_dir/'ML_teaching'/'user_data.csv'
logs_path = work_dir/'ML_teaching'/'logs.csv'

user_data = pd.read_csv(user_data_path)
logs = pd.read_csv(logs_path)

unique_platforms = logs.platform.value_counts()

true_success_count = logs.query('success==True')\
    .groupby('client', as_index=False)\
    .agg({'platform': 'count'})\
    .rename(columns={'platform': 'success_count'})\
    .sort_values('success_count', ascending=False)

max_success_count = true_success_count.success_count.max()
# обращение к переменной(колонке) которой нет в ДФ идет через @, tolist() - перевод в список
user_with_max_success_count = true_success_count\
    .query("success_count==@max_success_count")\
    .sort_values('client')\
    .client\
    .tolist()

print(user_with_max_success_count)

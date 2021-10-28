
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

true_success_count = logs\
    .query('success==True')\
    .groupby('client', as_index=False)\
    .agg({'platform': 'count'})\
    .rename(columns={'platform': 'success_count'})\
    .sort_values('success_count', ascending=False)
# альтернатива без query, если суммировать по колонке с булевыми знач, то учитываться будут только true
true_success_count = logs\
    .groupby('client', as_index=False)\
    .agg({'success': 'sum'})\
    .rename(columns={'success': 'success_count'})\
    .sort_values('success_count', ascending=False)


max_success_count = true_success_count.success_count.max()
# обращение к переменной(колонке) которой нет в ДФ идет через @, tolist() - перевод в список
user_with_max_success_count = true_success_count\
    .query("success_count==@max_success_count")\
    .sort_values('client')\
    .client\
    .tolist()

# перевод в строку через цикл c окончанием ", "
""" for user in user_with_max_success_count:
    print(user, end=', ') """

# альтернатива через: 'разделитель'.join[список строк] - внутри через for привели к строке
Str_user_max_success_count = ', '.join(
    [str(user) for user in user_with_max_success_count])

# С какой платформы было совершено наибольшее количество успешных операций
platform_max_true_success = logs\
    .groupby('platform', as_index=False)\
    .agg({"success": "sum"})\
    .rename(columns={"success": "success_count"})\
    .sort_values('success_count', ascending=False)\
    .platform\
    .head(1)

# Какую платформу предпочитают премиальные клиенты
full_data_client = user_data.merge(logs, on='client', how='inner')

premium_client_platform = full_data_client\
    .query('premium==True')\
    .groupby('platform', as_index=False)\
    .agg({'client': 'count'})\
    .rename(columns={'client': 'client_count'})\
    .sort_values('client_count', ascending=False)

# визуализация частоты распределения пользователей по возрастам, для обычных и премиум
# distplot(pd.серия, ax[i-номер строки сетки графиков], ...), const color = blue, red, yelow... kde-линия тренда
# fig, ax = plt.subplot(nrows = 2, ncols = 1) - создаст сетку графиков для одновременного отобр на разных сист коор

# sns.distplot(full_data_client.query('premium==False').age)
# sns.distplot(full_data_client.query('premium==True').age)

# график распределения числа успешных операций по клиентам
# show_success_dist.success.value_counts() - по сути визуализирует это
show_success_dist = logs\
    .groupby('client')\
    .agg({'success': 'sum'})
#sns.distplot(show_success_dist, kde=False)

# число успешных операций, сделанных на платформе computer

computer_success = full_data_client\
    .query('platform=="computer" and success==True')
# countplot - не требует группировки и агрегации, достаточно фильтра и указать какую перем считать
# аналогично можно реализовать через barplot(x,y) - в этом случае нужно сгруппировать по age, summ True_success
sns.countplot(x='age', data=computer_success)
plt.show()


# print(computer_success)

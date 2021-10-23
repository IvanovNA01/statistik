import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


path = r"C:\Users\IvanovNA01\Desktop\ВАЖНОЕ\datascience\statistic\statistik\statistik\ML_teaching\companies.csv"


def read_n_agg(path):
    df = pd.read_csv(path, sep=";").groupby('company').agg({"income": "mean"})
    return df


taxi = pd.read_csv(
    r"C:\Users\IvanovNA01\Desktop\ВАЖНОЕ\datascience\statistic\statistik\statistik\ML_teaching\taxi_peru.csv", sep=";", parse_dates=['start_at', 'end_at', 'arrived_at'])
# возвращает серию колич уник значений по каждому типу  source
count_platform = taxi['source'].value_counts()
""" 
iPhone     9741
web        7631
Android    4909
iPad        571
Wap         136
Name: source, dtype: int64 """
# макс по колич уник значений типа source в %
max_perc_source = round(
    taxi['source'].value_counts().max()*100/taxi['source'].count(), 0)
# аналогично
# value_counts(normalize=True) - возвращает долю от общего, dropna=True - не учитывать NA
# mul(100) = *100 - делается для удобства накладывания ф-ий
max_perc_source = taxi['source'].value_counts(
    normalize=True, dropna=True).mul(100).max().round()
# .reset_index() – сбросить индекс (переводит индексы в разряд 1 колонки)
driver_score_counts = taxi.driver_score.value_counts(
    normalize=True).mul(100).round(2).reset_index()\
    .rename(columns={'driver_score': 'percentage', "index": "driver_score"})\
    .sort_values('driver_score', ascending=False)
# визуализация
# plt.subplots - позволяет построить несколько диаграмм одновременно с помощью seaborn
# первый – количество строк, второй – количество столбцов, третий – количество диаграмм
fig, ax = plt.subplots(1, 2)

ax[0] = sns.barplot(x='driver_score', y='percentage',
                    data=driver_score_counts, color='blue', alpha=0.5, ax=ax[0])
ax[0].set(xlabel='Driver score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
# plt.show()

rider_score_counts = taxi.rider_score.value_counts(
    normalize=True).mul(100).round(2).reset_index()\
    .rename(columns={'rider_score': 'percentage', "index": "rider_score"})\
    .sort_values('rider_score', ascending=False)

ax[1] = sns.barplot(x='rider_score', y='percentage',
                    data=rider_score_counts, color='red', alpha=0.5, ax=ax[1])
ax[1].set(xlabel='rider score', ylabel='Percentage')
sns.despine()  # убрать часть рамки графика
plt.show()

# fig.show()

# print(rider_score_counts)

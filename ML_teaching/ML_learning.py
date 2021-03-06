import pandas as pd
from pandas.io.parsers import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np
from pathlib import Path

work_dir = Path.cwd()
StudentsPerformance_path = work_dir/'ML_teaching'/'StudentsPerformance.csv'
StudentsPerformance = read_csv(StudentsPerformance_path)
Dota_hero_path = work_dir/'ML_teaching'/'dota_hero_stats.csv'
Dota_hero = read_csv(Dota_hero_path)

#!!! ИСПОЛЬЗОВАНИЕ LOC ILOC
# iloc - обращение по индексам выбираем 3,6,13, последнюю строки и 3-5 столбцы (нумирация с 0)
df_with_names = StudentsPerformance.iloc[[3, 5, 12, -1], 2:5]
# присваиваем индексам имена
df_with_names.index = ['bob', 'stan', 'jone', 'dastin']
# loc - обращение по именованным индексам и просто индексам (строки 'bob','jone' и все столбцы)
#!!! loc берёт строки включая последнюю, а iloc нет
df_with_names_loc = df_with_names.loc[['bob', 'jone'], :]
# все строки, все столбцы кроме вычтенных
score_list = [i for i in list(StudentsPerformance) if 'score' in i]
df_without_columns_loc = StudentsPerformance\
    .loc[:, ~StudentsPerformance.columns.isin(score_list)]
print(df_without_columns_loc)
# переменная внутри запроса
mean_writing_score = StudentsPerformance['writing score'].mean()
filter_student = StudentsPerformance\
    .loc[StudentsPerformance['writing score'] > mean_writing_score]
# для объединения булевых условий необходимо исп (), логические объединения & вместо and и т.д.(результат пустой дф!)
double_filter_StPer = StudentsPerformance[(
    StudentsPerformance['writing score'] > 100) & (StudentsPerformance.gender == 'female')]
# переменная с запросом
filter_query = (StudentsPerformance['writing score'] >= 80) & (
    StudentsPerformance.gender == 'male')
male_80_StPer = StudentsPerformance.loc[filter_query]
# У какой доли студентов из датасэта в колонке lunch указано free/reduced
part_student_StPer = StudentsPerformance.lunch.value_counts(normalize=True)

# среднее и дисперсия оценок по предметам у групп студентов со стандартным или урезанным ланчем
"""
gender                         object
race/ethnicity                 object
parental level of education    object
lunch                          object
test preparation course        object
math score                      int64
reading score                   int64
writing score                   int64

gender race/ethnicity parental level of education         lunch test preparation course  math score  reading score  writing score
0  female        group B           bachelor's degree      standard                    none          72             72             74
1  female        group C                some college      standard               completed          69             90             88
2  female        group B             master's degree      standard                    none          90             95             93
3    male        group A          associate's degree  free/reduced                    none          47             57             44
4    male        group C                some college      standard                    none          76             78             75
"""
standard_lunch = (StudentsPerformance.lunch == "standard")
mean_std_standard_student = StudentsPerformance\
    .loc[standard_lunch == True, ['math score',  'reading score',  'writing score']]\
    .describe()

"""    math score  reading score  writing score
count  645.000000     645.000000     645.000000
mean    70.034109      71.654264      70.823256
std     13.653501      13.830602      14.339487
min     19.000000      26.000000      22.000000
25 % 61.000000      63.000000      62.000000
50 % 69.000000      72.000000      72.000000
75 % 80.000000      82.000000      81.000000
max    100.000000     100.000000     100.000000 """

mean_std_free_student = StudentsPerformance\
    .loc[standard_lunch == False, ['math score',  'reading score',  'writing score']]\
    .describe()
"""    math score  reading score  writing score
count  355.000000     355.000000     355.000000
mean    58.921127      64.653521      63.022535
std     15.159956      14.895339      15.433823
min      0.000000      17.000000      10.000000
25 % 49.000000      56.000000      53.000000
50 % 60.000000      65.000000      64.000000
75 % 69.000000      75.000000      74.000000
max    100.000000     100.000000     100.000000 """

# уберем пробелы и заглавные из колонок


def Lower_replace_columns(old_columns):
    new_columns = old_columns.replace(" ", "_").lower()
    return new_columns


# !!! При передаче ф-ии в качестве аргумента rename указываем ТОЛЬКО имя ф-ии
StudentsPerformance = StudentsPerformance.rename(columns=Lower_replace_columns)

""" gender race/ethnicity parental_level_of_education         lunch test_preparation_course  math_score  reading_score  writing_score  Sum_score   log_sum
0    female        group B           bachelor's degree      standard                    none          72             72             74        218  5.384495
1    female        group C                some college      standard               completed          69             90             88        247  5.509388
2    female        group B             master's degree      standard                    none          90             95             93        278  5.627621
3      male        group A          associate's degree  free/reduced                    none          47             57             44        148  4.997212
4      male        group C                some college      standard                    none          76             78             75        229  5.433722
..      ...            ...                         ...           ...                     ...         ...            ...            ...        ...       ...
995  female        group E             master's degree      standard               completed          88             99             95        282  5.641907
996    male        group C                 high school  free/reduced                    none          62             55             55        172  5.147494
997  female        group C                 high school  free/reduced               completed          59             71             65        195  5.273000
998  female        group D                some college      standard               completed          68             78             77        223  5.407172
999  female        group D                some college  free/reduced                    none          77             86             86        249  5.517453
 """

#!!! ISIN - вызывает значения которые входят в isin для данной колонки
# StudentsPerformance[StudentsPerformance['parental_level_of_education'].isin(["bachelor's degree", "master's degree"])]

#!!! ФИЛЬТРАЦИЯ ПО ЧАСТИ ИМЕНИ СТРОКИ/СТОЛБЦА - filter(like='часть имени', axis = 0-строка/1-столбец)
# [n for n in range(1, 20) if n % 2 == 0] - список из n таких что n входит в range(1, 20) при условии n % 2 == 0
# Списковые включения могут использовать вложенные итерации по переменным:
[(x, y) for x in range(1, 10) for y in range(1, 10) if x % y == 0]
#!!! [(1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4), (5, 1), (5, 5), (6, 1), (6, 2),
#!!! (6, 3), (6, 6), (7, 1), (7, 7), (8, 1), (8, 2), (8, 4), (8, 8), (9, 1), (9, 3), (9, 9)]
# Сумма чётных чисел из range(1, 10000):
sum(n for n in range(1, 10000) if n % 2 == 0)
# Python предоставляет аналогичные возможности для создания множеств и словарей.
{x for x in range(10)}
#!!! {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{x: x**2 for x in range(10)}
#!!! {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# вариант на питоне-> score_list =  [i for i in list(df_with_names) if 'score' in i] - список из i: i лежит в списке колонок, при условии что в них есть 'score'
# вариант на питоне-> df_with_names[score_list] - вывод ДФ с колонками определенными в score_list
rows_withe_e_names = df_with_names.filter(like='e', axis=0)
# add new column = sum all collumns with title like 'score' (axis=1) -> суммирует по колонкам
StudentsPerformance['Sum_score'] = StudentsPerformance.filter(
    like='score').sum(axis=1)

# assign добавление новых колонок, с созданием нового ДФ (старый не трогает пока не присвоим)
StudentsPerformance = StudentsPerformance.assign(
    log_sum=np.log(StudentsPerformance.Sum_score))
# drop удаление новых колонок, с созданием нового ДФ (старый не трогает пока не присвоим)

#!!! ЛЯМБДА ВНУТРИ АГРЕГАЦИИ
StudentsPerformance.groupby('gender')\
    .aggregate({'Sum_score': lambda x: max(x) - min(x)})
"""     Sum_score
gender
female        273
male          231
 """

Titanic_path = work_dir/'ML_teaching'/'titanic.csv'
titanic_df = read_csv(Titanic_path)

titanic_shape = titanic_df.shape
Titan_dtipes = titanic_df.dtypes
# объединяет инфу по предыдущим атрибутам
titanic_info = titanic_df.info()


#!!! ВИЗУАЛИЗАЦИЯ
# plt.subplots - позволяет построить несколько диаграмм одновременно с помощью seaborn
# первый – количество строк, второй – количество столбцов, третий – количество диаграмм
plt.subplot(1, 2, 1)
# линейная корреляция Х относительно У, hue-группировка
sns.lmplot(x='math_score', y='reading_score',
           hue='gender', data=StudentsPerformance)
plt.subplot(1, 2, 2)
sns.histplot(StudentsPerformance["math_score"])
plt.subplot(1, 3, 3)
sns.heatmap(StudentsPerformance.corr(), vmin=-1, vmax=1, annot=True)
# plt.show()

#print(StudentsPerformance.groupby('gender').aggregate({'Sum_score': lambda x: max(x) - min(x)}))

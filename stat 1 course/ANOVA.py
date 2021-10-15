from scipy.stats import f_oneway, t  # Подсчет значения F-критерия
# предоставляет классы и функции для оценки множества различных статистических моделей,
import statsmodels.api as sm
# а также для проведения статистических тестов и исследования статистических данных
from statsmodels.formula.api import ols
# строится поверх библиотеки NumPy, являющейся инструментом более низкого уровня.
import pandas as pd
# Предоставляет специальные структуры данных и операции для манипулирования числовыми таблицами и временными рядами
import matplotlib.pyplot as plt  # предназначена для создания научной графики
import seaborn as sns  # пакет визуализации различными графиками
# пакет научных и инженерных библиотек, статистических и других методов(из пакета scipy класс stats)
import scipy.stats as st

""" # Подсчет значения F-критерия для трех групп - Однофакторный дисперсионный анализ(сравнение групп на принадлежность одной ГС) """
F, p = f_oneway([3, 1, 2], [5, 3, 4], [7, 6, 5])
print("F-value is {}, P={}%".format(F, p*100))
print(p)

""" Визуализация средних значений и дов интер 4х выборок """
# var-1
# визуализация таблицы рассчетных значений Однофакторного дисперсионного анализа
df = pd.read_csv('genetherapy.csv')
lm = ols('expr ~ Therapy', data=df).fit()
table = sm.stats.anova_lm(lm)
table

sns.set_theme(style='darkgrid')
sns.pointplot(x='Therapy', y='expr', data=df)
plt.show()

# var-2
# выставляем уровень значимости
p = 0.95

# обрабатываем сырые данные из csv файла, находим объем, среднее и стандартное отклонение выборки
data = pd.read_csv("genetherapy.csv", sep=',')
data_agg = data.groupby(['Therapy']).agg(['count', 'mean', 'std'])

""" Альтернатива считывания данных
URL = 'https://stepik.org/media/attachments/lesson/8083/genetherapy.csv'
data = pd.read_csv(URL)
A = data[data["Therapy"] == "A"]["expr"]
B = data[data["Therapy"] == "B"]["expr"]
C = data[data["Therapy"] == "C"]["expr"]
D = data[data["Therapy"] == "D"]["expr"]
#расчет F-критерия и его вероятности 
F, p = f_oneway(A,B,C,D)
# Находим среднее для всех терапий
data.groupby('Therapy')['expr'].mean() """

# для каждой выборки высчитываем интервал по формуле для t-распределения: (K * se), где
# K t-value, зависит от степеней свободы df = n-1 и целевого значения вероятности p,
# se - стандартная ошибка среднего = std/sqrt(n), std - стандартное отклонение выборки, n - количество элементов
data_agg['interval'] = t.ppf((1 + p)/2, data_agg['expr']['count']-1) * \
    data_agg['expr']['std']/(data_agg['expr']['count'] ** .5)

# cтроим доверительные интервалы на графике
plt.errorbar(x='Therapy ' + data_agg.index, y=data_agg['expr']['mean'], yerr=data_agg['interval'],
             color="black", capsize=3, marker="s", markersize=4, mfc="red", mec="black", fmt='o')
plt.title('Уровень экспрессии гена при различной терапии')
plt.grid()
plt.xlabel('therapy')
plt.ylabel('Уровень экспрессии')
plt.show()

""" еще одна альтернатива
p = 0.95

data = pd.read_csv("C:\MyCode\Python\Statistics\genetherapy.csv", sep=',')
data_agg = data.groupby(['Therapy']).agg(['count', 'mean', 'std'])
data_agg = data_agg.droplevel(0, axis=1)


# Переименовываем колонки, чтобы программа не воспринимала их как названия функций
data_agg.rename(columns={'count': 'N', 'mean': 'Mean',
                'std': 'Std'}, inplace=True)

data_agg['se'] = data_agg.Std.div(data_agg.N ** 0.5)

# Расчет полуширины доверительного интервала
data_agg['K'] = data_agg.apply(lambda x: t.interval(p, x.N-1, loc=x.Mean, scale=x.se)[1],
                               axis=1) - data_agg.Mean
# Строим график
plt.errorbar(x='Therapy ' + data_agg.index, y=data_agg.Mean, yerr=data_agg.K,
             color="black", capsize=3, marker="s", markersize=4, mfc="red", mec="black", fmt='o')
plt.title('Уровень экспрессии гена при различной терапии')
plt.grid()
plt.xlabel('therapy')
plt.ylabel('Уровень экспрессии')
plt.show() """

# расчет вероятности F-критерия для группы,
# F=значение F-критерия, df_ssb - степень свободы межгрупповая = m-1 (m-кол групп), df_ssw - степень свободы внутригрупповая = N-m (N-общее число значение)
# print(st.f.sf(F, df_ssb, df_ssw)) в процентах
print(st.f.sf(3.5, 3, 16))

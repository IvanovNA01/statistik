# вариант с 2 параметричискими критериями, у sex - 2 градации, у pclass - 3, survived - ЗП

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

category_columns = {
    col: "category" for col in ["Survived", "Sex", "Pclass"]
}  # приведение
# выбранных колонок к категориальному

df = pd.read_csv(
    "https://stepic.org/media/attachments/course/524/train.csv", dtype=category_columns
)

df_full = pd.read_csv(
    "https://stepic.org/media/attachments/course/524/train.csv"
)
print(df_full.head())

# дропнули все NA
data = df[df.Age.notnull()]

# Зависимая переменная обычно обозначается как "Y" или "y"
Y = data.loc[:, "Survived"].cat.codes

# переменные с градациями трансформированы
X = sm.add_constant(data.loc[:, "Sex"].cat.codes)
X = sm.add_constant(data.loc[:, "Pclass"].cat.codes)

# ВЫЧИСЛЯЕМ
#
# Классическое представление результат-предиктор(ы),
# которое используется в классификаторах
glm_binom = sm.GLM(Y, X, family=sm.families.Binomial())
res = glm_binom.fit()

# Можно и так (кто привык к R)
glm_binom_rstyle = smf.glm(
    formula="Survived ~ Sex * Pclass", data=data, family=sm.families.Binomial()
)
res_rstyle = glm_binom_rstyle.fit()
""" 
категориальный тип переменных можно указать в формуле следующим образом:
model = smf.logit(formula = 'Survived ~ C(Sex) * C(Pclass)', data = df).fit()
и знак при коэффициентах не будет обратным """

print(res.summary())
print(res_rstyle.summary())


""" сокращенный вариант
# в предыдущем не удалил лишнее.
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# приведение # выбранных колонок к категориальному
category_columns = {col: 'category' for col in ['Survived',
                                                'Sex',
                                                'Pclass']}

df = pd.read_csv('https://stepic.org/media/attachments/course/524/train.csv',
                 dtype=category_columns)

# дропнули все NA
data = df[df.Age.notnull()]

# ВЫЧИСЛЯЕМ
glm_binom_rstyle = smf.glm(formula="Survived ~ Sex * Pclass", data=data,
                           family=sm.families.Binomial())
res_rstyle = glm_binom_rstyle.fit()

print(res_rstyle.summary()) """

# создание таблицы для Ж
""" 
Pclass  Survived
1       Yes         82
2       Yes         68
3       No          55
        Yes         47
2       No           6
1       No           3
dtype: int64

data = pd.read_csv("https://stepic.org/media/attachments/course/524/train.csv")
data = data[data.Age.notnull()]  # Удаляем нулевые значения в возрасте

d = data[["Sex", "Pclass", "Survived"]]  # Вырезаем нужные нам столбцы
d.loc[d["Survived"] == 0, "Survived"] = "No"
d.loc[d["Survived"] == 1, "Survived"] = "Yes"
d.value_counts()["female"]  # Для женщин
# d.value_counts()['male'] # Для мужчин """

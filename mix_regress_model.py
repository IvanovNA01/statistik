import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# грузим датасет
url = "https://raw.githubusercontent.com/razority/R_data/main/Exam.xlsx"
exam = pd.read_excel(url)
exam["school"] = exam["school"].map(lambda x: str(x))

# рисуем диаграмму рассеяния
fig, ax = plt.subplots(figsize=(8, 8))
g = sns.scatterplot(x="standLRT", y="normexam", hue="school", data=exam)
# немного надо трансформировать легенду
h, l = g.get_legend_handles_labels()
g.legend(h, l, ncol=4, bbox_to_anchor=(1, 1), loc=2)

# исследуем модель
model = smf.ols("normexam ~ standLRT", data=exam).fit()
display(model.summary())

# линейная регрессия
plt.figure(figsize=(8, 8))
x = np.array(exam.loc[:, "standLRT"])
y = np.array(exam.loc[:, "normexam"])

sns.scatterplot(x="standLRT", y="normexam", data=exam)
b1, b0 = np.polyfit(x, y, 1)  #  b0 - intercept, b1 - slope
sns.lineplot(x, b0 + b1 * x, color="red")
plt.grid()

""" Вот так выглядят регрессионные модели, если их строить отдельно для каждой школы.
ggplot(data = Exam, aes(x = standLRT, y = normexam)) +
  geom_point(alpha = 0.3) +
  geom_smooth(aes(color=school), method = 'lm', se = FALSE) """

vc = "normexam ~ standLRT"
model2 = smf.mixedlm(vc, data=exam, groups=exam["school"]).fit()
display(model2.summary())

plt.figure(figsize=(8, 8))
X2 = np.array(exam.loc[:, "standLRT"])
y2 = np.array(exam.loc[:, "normexam"])

sns.scatterplot(x="standLRT", y="normexam", data=exam, alpha=0.3)

# задаём только intercept для каждой школы
for school in exam["school"].unique():
    X2 = np.array(exam[exam["school"] == school].loc[:, "standLRT"])
    y2 = np.array(exam[exam["school"] == school].loc[:, "normexam"])
    b01, b00 = np.polyfit(
        X2, y2, 1
    )  #  b00 - intercept for school , b01 - slope for school
    sns.lineplot(X2, b00 + b1 * X2, legend="full", label=school)

plt.legend(ncol=3, bbox_to_anchor=(1.0, 1.0))
plt.grid()

# ********************************

plt.figure(figsize=(8, 8))
sns.scatterplot(x="standLRT", y="normexam", data=exam, alpha=0.3)

# задаём только и slope и intercept для каждой школы
for school in exam["school"].unique():
    X2 = np.array(exam[exam["school"] == school].loc[:, "standLRT"])
    y2 = np.array(exam[exam["school"] == school].loc[:, "normexam"])
    b01, b00 = np.polyfit(
        X2, y2, 1
    )  #  b00 - intercept for school , b01 - slope for school
    sns.lineplot(X2, b00 + b01 * X2, legend="full", label=school)

plt.legend(ncol=3, bbox_to_anchor=(1.0, 1.0))
plt.grid()


import pandas as pd
import statsmodels.formula.api as smf

# грузим датасет
url = "https://raw.githubusercontent.com/razority/R_data/main/Exam.xlsx"
exam = pd.read_excel(url)
exam["school"] = exam["school"].map(lambda x: str(x))


# normexam ~ standLRT + (1|school) - случай когда учитываем влияние только интерсепта случайного эффекта
model2 = smf.mixedlm("normexam ~ standLRT", data=exam, groups=exam["school"]).fit()
display(model2.summary())


# normexam ~ standLRT + (1 + standLRT|school) - случай когда учитываем влияние интерсепта и слоупа случайного эффекта, на НП
model3 = smf.mixedlm(
    "normexam ~ standLRT", data=exam, groups=exam["school"], re_formula="~standLRT"
).fit()
display(model3.summary())

# normexam ~ standLRT + (1|school) + (0 + standLRT|school) - случай когда учитываем влияние интерсепта и слоупа случайного эффекта, на НП
# но нет корреляции между случайными эффектами

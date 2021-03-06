import pandas as pd
from statsmodels.graphics.factorplots import interaction_plot
from scipy import stats

data = pd.read_csv("C:\Users\Espad\Projects\python\statistik\stat 1 course\atherosclerosis.csv", sep=",")
# Картинка
fig = interaction_plot(
    data.dose, data.age, data.expr, colors=["green", "red"], markers=["D", "^"], ms=10
)
# Степени свободы
# общ кол-во зависимых переменных
N = len(data.expr)
# количество групп по каждому из факторов
m1 = len(data.age.unique())
m2 = len(data.dose.unique())
# степени свободы межгрупповые для каждой группы
df_a = m1 - 1
df_b = m2 - 1
df_axb = df_a * df_b
# внутригрупповые
df_w = N - m1 * m2
# Общее среднее
grand_mean = data["expr"].mean()
# Суммы квадратов
ssq_a = sum([(data[data.age == i].expr.mean() - grand_mean) ** 2 for i in data.age])
ssq_b = sum([(data[data.dose == i].expr.mean() - grand_mean) ** 2 for i in data.dose])
ssq_total = sum((data.expr - grand_mean) ** 2)
# разделение по возрасту
spl_age = [data[data.age == i] for i in data.age.unique()]
age_means = [
    [x_age[x_age.dose == d].expr.mean() for d in x_age.dose] for x_age in spl_age
]
ssq_w = sum(
    [sum((spl_age[i].expr - age_means[i]) ** 2) for i in range(len(data.age.unique()))]
)
ssq_axb = ssq_total - ssq_a - ssq_b - ssq_w
# Средние квадраты
ms_a = ssq_a / df_a
ms_b = ssq_b / df_b
ms_axb = ssq_axb / df_axb
ms_w = ssq_w / df_w
# F-значения
f_a = ms_a / ms_w
f_b = ms_b / ms_w
f_axb = ms_axb / ms_w
# P-значения
p_a = stats.f.sf(f_a, df_a, df_w)
p_b = stats.f.sf(f_b, df_b, df_w)
p_axb = stats.f.sf(f_axb, df_axb, df_w)
# результаты
results = {
    "sum_sq": [ssq_a, ssq_b, ssq_axb, ssq_w],
    "df": [df_a, df_b, df_axb, df_w],
    "F": [f_a, f_b, f_axb, "NaN"],
    "PR(>F)": [p_a, p_b, p_axb, "NaN"],
}
columns = ["sum_sq", "df", "F", "PR(>F)"]
aov_table1 = pd.DataFrame(
    results, columns=columns, index=["age", "dose", "age:dose", "Residual"]
)
print(aov_table1)

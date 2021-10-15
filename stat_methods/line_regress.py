import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

URL = "http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv"
df = pd.read_csv(URL)
x = df["hs_grad"]
y = df["poverty"]
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
mn = np.min(x)
mx = np.max(x)
x1 = np.linspace(mn, mx, 500)
y1 = gradient * x1 + intercept
plt.title("Связь бедности и уровня образования")
plt.xlabel("Уровень образования %")
plt.ylabel("Уровень бедности %")
plt.plot(x, y, "ob")  # Рассталяем точки
plt.plot(x1, y1, "-r")  # Рисуем линию
plt.show()  # Рисуем график
stats.linregress(x, y)

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

data = pd.read_csv(
    "http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv"
)

data_crop = data[["white", "hs_grad", "poverty"]]
data_crop.head()
white, hs_grad, poverty = [column for column in data_crop.values.T]

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(xs=white, ys=poverty, zs=hs_grad)

ax.set_xlabel("White(%)")
ax.set_ylabel("Poverty(%)")
ax.set_zlabel("Higher education(%)")

plt.show()

""" ВАРИАНТ С ВИЗУАЛИЗАЦИЕЙ ПЛОСКОСТИ

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('http://d396qusza40orc.cloudfront.net/statistics/lec_resources/states.csv')

X = data[['white', 'hs_grad']]
y = data['poverty']

reg = LinearRegression().fit(X, y)

d1, d2 = list(), list()
for x in np.linspace(min(data['white']), max(data['white']), 100):
    for y in np.linspace(min(data['hs_grad']), max(data['hs_grad']), 100):
        d1.append(x)
        d2.append(y)
d1 = np.array(d1).reshape(-1, 1)
d2 = np.array(d2).reshape(-1, 1)
p = reg.predict(np.concatenate([d1, d2], axis=1))


fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

ax.scatter(data['hs_grad'], data['white'], data['poverty'], s=50)

ax.plot_trisurf(d2.ravel(), d1.ravel(), p.ravel(), alpha=0.2)

ax.set_xlabel('Higher education(%)')
ax.set_ylabel('White(%)')
ax.set_zlabel('Poverty(%)')

ax.elev = 10
ax.azim = -60

plt.show() """

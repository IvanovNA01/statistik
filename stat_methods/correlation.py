from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


def cortest(corr, lenX):
    # t value
    t = corr[0] * ((len(X) - 2) / (1 - corr[0] ** 2)) ** 0.5
    print("data: x and y")
    print(
        "t = {}, df = {}, p-value = {}".format(
            round(t, 5), len(X) - 2, round(stats.t.sf(np.abs(t), 48) * 2, 5)
        )
    )

    # Use the Fisher transformation to get z
    z = np.arctanh(corr[0])
    # print("z value: {}".format(z))

    # And, the sigma value i.e standard error
    sigma = 1 / ((len(X) - 3) ** 0.5)
    # print("sigma value: {}".format(sigma))

    # Get normal 95% interval probability density function for normal continuous random variable apply two-sided conditional formula
    cint = z + np.array([-1, 1]) * sigma * stats.norm.ppf((1 + 0.95) / 2)

    # Finally take hyperbolic tangent to get interval values for 95%
    interval = np.tanh(cint)

    if corr != 0:
        print("alternative hypothesis: true correlation is not equal to 0")
    print("95 percent confidence interval:")
    print(interval)
    print("sample estimates:")
    print("cor")
    print(corr[0])


# вычисляем корреляцию
X = stats.norm.rvs(loc=0, scale=1, size=50)
Y = stats.norm.rvs(loc=0, scale=1, size=50)
corr = stats.pearsonr(X, Y)

# строим scatter plot- диаграмма рассеивания
plt.scatter(X, Y)
plt.grid()
plt.show()

# print("correlation: {}".format(corr))

# т.к. из лекции мы не знаем выборки, то сразу подставляем корреляцию из лекции
cortest((0.2858888,), 50)

""" пример расчета корреляции """
X = np.array([4, 5, 2, 3, 1])
Y = np.array([2, 1, 4, 3, 5])
X_mean = np.mean(X)
Y_mean = np.mean(Y)
X_sum_std_test = 0
for i in range(5):
    X_sum_std_test += (X[i] - X_mean) ** 2

X_std_test_1 = np.sqrt(X_sum_std_test / 5)

X_std_test = np.sqrt(sum([(X[i] - X_mean) ** 2 for i in range(5)], 0))
Y_std_test = np.sqrt(sum([(Y[i] - Y_mean) ** 2 for i in range(5)], 0))

X_std = np.std(X)
Y_std = np.std(Y)
sumCOVAR = 0
for i in range(5):
    sumCOVAR += (X[i] - X_mean) * (Y[i] - Y_mean)
    print(sumCOVAR)

# ковариационная матрица
Cov = np.cov(X, Y)
print(Cov)
Kor = sumCOVAR / (X_std_test * Y_std_test)
Kor_stats = stats.pearsonr(X, Y)
print(Kor)
print(Kor_stats)

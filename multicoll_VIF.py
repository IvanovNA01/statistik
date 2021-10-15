import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from patsy import dmatrices

%matplotlib inline

url = 'https://gist.githubusercontent.com/christophsax/178d34245afdd6e187b1fff72dbe7448/raw/f5f4189f949f117bee4e82e4aa75c104ed20b4f4/swiss.csv'
data = pd.read_csv(url)
data.rename(columns={'Infant.Mortality': 'Mortality'}, inplace=True)


# сравнение по матрице регресии
axes = pd.plotting.scatter_matrix(data, figsize=(10,10), diagonal='kde', grid=True)
corr = data.corr()

# это для крассивой аннотации
for i, j in zip(*plt.np.triu_indices_from(axes, k=1)):
    value = corr.values[i,j]
    if abs(value) <= 0.25:
        fontsize = 14
    else:
        fontsize = round(56*abs(value))
    axes[i, j].annotate(
        "%.2f" %value, (0.5, 0.5), xycoords='axes fraction'
        , ha='center', va='center', fontsize=fontsize
    )
plt.show()

print(corr)


# рассчитываем VIF
predictors = " + ".join(list(
    set(data.columns) - set(['Fertility', 'Location'])
    ))
y, X = dmatrices('Fertility ~' + predictors, data, return_type='dataframe')


vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
print(f'\nVIF:\n{vif.T}')
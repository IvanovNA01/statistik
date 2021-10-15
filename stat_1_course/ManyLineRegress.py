import numpy as np
import pandas as pd

import statsmodels.formula.api as sm


data = pd.read_csv("states.csv")
# обычные наименьшие квадраты - это тип линейного метода для оценки неизвестных параметров в модели линейной регрессии
result = sm.ols(
    formula="poverty ~ metro_res + white + hs_grad + female_house", data=data
).fit()


print(result.params)
print(result.summary())

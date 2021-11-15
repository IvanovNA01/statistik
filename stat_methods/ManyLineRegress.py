import numpy as np
import pandas as pd

import statsmodels.formula.api as sm
from pathlib import Path

work_dir = Path.cwd()
states_path = work_dir/'stat_methods'/'states.csv'

data = pd.read_csv(states_path)
# обычные наименьшие квадраты - это тип линейного метода для оценки неизвестных параметров в модели линейной регрессии
result = sm.ols(
    formula="poverty ~ metro_res + white + hs_grad + female_house", data=data
).fit()


print(result.params)
print(result.summary())

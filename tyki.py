from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)
import pandas as pd
data_stepik = pd.read_csv(
    'https://stepik.org/media/attachments/lesson/8083/genetherapy.csv')

MultiComp = MultiComparison(data_stepik['expr'], data_stepik['Therapy'])

print(MultiComp.tukeyhsd().summary())

import pandas as pd
from pandas.io.parsers import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

work_dir = Path.cwd()
StudentsPerformance_path = work_dir/'ML_teaching'/'StudentsPerformance.csv'
StudentsPerformance = read_csv(StudentsPerformance_path)

print(StudentsPerformance.head(5))

import pandas as pd
import numpy as np

Salary = np.array([30000, 40000, 45000, 50000, 55500, 60000, 70000, 80000, 90000, 100000])

df=pd.DataFrame(data=Salary, columns=['Salary'])
print(df)
import numpy as np
import pandas as pd
from scipy import stats

# make the data 
data = [2.5, 2.7, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 110.0]

# find the z-score of each data point
z_scores = np.abs(stats.zscore(data))

# threshold for outliar
threshold = 2.5

# get the indices of outliars from z-score list
outliar_indices = np.where(z_scores > threshold)[0]
print('Outliar Indices',outliar_indices)

print("Data\n",data)
print("Outliars in Data\n", [data[index] for index in outliar_indices])
print("Data After Removing Outliars")
data = [data[index] for index in range(len(data)) if index not in outliar_indices]
print(data)
        
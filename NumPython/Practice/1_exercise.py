'''
Problem: Create a 2D NumPy array of shape (5, 5) with random integers between 1 and 100. Then, perform the following tasks:
Find the sum of all elements in the array.
Calculate the mean of each column.
Find the maximum value in each row.
Create a new array containing only the elements from the original array that are greater than 50.
Replace all even numbers in the original array with 0.
'''

import numpy as np
arr = np.array([[5,10,60,20,25],
               [30,35,40,45,50],
               [52,25,30,58,60],
               [55,60,65,70,75],
               [80,85,90,95,100]])
print(arr[-1])

print('========Part 1=========')
print(f'Sum of all elements : {np.sum(arr)}')

print('========Part 2=========')
# The syntax arr[:, 0] uses slicing. Let's analyze it:
# arr[:, 0]
# The colon : means: "select all rows"
# The 0 means: "select column at index 0
for i in range(arr.shape[1]):
    row = np.mean(arr[:,i])
    print(f'Mean of {i+1} col : {row}')

print('========Part 3=========')
for i in range(arr.shape[0]):
    row = np.max(arr[i,:])
    print(f'Max of {i+1} row : {row}')
    
print('========Part 4=========')
arr_max = np.array([])  
for i in range(arr.shape[0]):      # Loop over each row
    for j in range(arr.shape[1]):   # Loop over each column
        if arr[i][j] > 50:          # check agar is position pe element greater than 50 ha to new array ma append karde.
            arr_max = np.append(arr_max, arr[i][j])
print(arr_max)

print('========Part 5=========')
# Replace all even numbers in the original array with 0.
for i in range(arr.shape[0]):  # range = 4 means '5 rows' from 0-4
    for j in range(arr.shape[1]):   # range = 4 means '5 colums in a row' from 0-4
            if arr[i][j] % 2 == 0:
                arr[i][j] = 0

print(arr)


    
    
    
    
    
    











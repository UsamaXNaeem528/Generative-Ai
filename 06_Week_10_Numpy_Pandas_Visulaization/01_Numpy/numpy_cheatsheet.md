# NumPy Cheat Sheet

## Import
```python
import numpy as np
```

## Creating Arrays
```python
np.array([1,2,3])                  # 1D array
np.array([[1,2,3],[4,5,6]])        # 2D array
np.array([[[1,2],[3,4]],[[5,6],[7,8]]])  # 3D array (stack of 2D arrays)

np.zeros((2,3))                    # filled with 0
np.ones((3,3))                     # filled with 1
np.full((3,4), 9)                  # filled with a custom value
np.arange(start, stop, step)       # sequence, e.g. np.arange(1,20,3)
np.eye(3)                          # identity matrix (n x n, 1s on diagonal)
```

## Array Properties
```python
arr.ndim        # number of dimensions
arr.shape       # (rows, cols, ...)
arr.size        # total number of elements
arr.dtype       # data type of elements
arr.astype(int) # convert/cast to a new dtype (returns copy)
```
> `<U2` dtype = string data. Use `.astype(int)`/`.astype(float)` to convert.

## Arithmetic (element-wise, no loops needed)
```python
arr + 2
arr * 2
arr / 2
arr ** 2
arr % 2
```

## Aggregation Functions
```python
arr.sum()
arr.mean()      # average
arr.min()
arr.max()
arr.var()       # variance: spread of data (squared units)
arr.std()       # standard deviation: spread of data (original units)
```

## Indexing
```python
arr[2]          # 1D: 3rd element
arr[-2]         # negative indexing (from the end)
arr2d[1]        # 2D: entire row at index 1
```

## Slicing — `array[start:stop:step]`
```python
arr[0:5]        # elements 0 to 4 (stop excluded)
arr[0::2]       # every 2nd element
arr[2:5:2]      # start=2, stop=5, step=2
arr[-1::-1]     # reverse the array (no loop!)
```

## Fancy Indexing
```python
arr[[0, 2, 4]]  # select multiple specific indices at once (returns a copy)
```

## Boolean Masking / Filtering
```python
arr[arr % 2 == 0]     # keep only elements where condition is True
```

## Reshaping
```python
arr.reshape(2, 3)     # total elements must stay the same (2*3 = original size)
                       # returns a VIEW → changes affect the original array too
```

## Flattening (N-D → 1D)
```python
arr2D.ravel()          # returns a VIEW (shares memory, changes affect original)
arr2D.flatten()        # returns a COPY (changes do NOT affect original)
```

## Insert / Append / Concatenate / Delete
```python
np.insert(arr, index, value)              # 1D insert (returns new array)
np.insert(arr2d, 1, [5,7,9], axis=0)      # insert row
np.insert(arr2d, 1, [5,7], axis=1)        # insert column

np.append(arr, [values])                  # add to the end
np.append(arr2d, [[7],[8]], axis=1)       # append column(s)

np.concatenate((arr1, arr2), axis=0)      # join arrays along an axis

np.delete(arr, index)                     # delete by index (1D)
np.delete(arr2d, 1, axis=1)               # delete a column (2D)
```

## Stacking
```python
np.vstack((arr1, arr2))    # vertical: stack rows (adds rows, goes downward)
np.hstack((arr1, arr2))    # horizontal: stack columns (adds columns, goes rightward)
```

## Splitting
```python
np.split(arr, 3)           # split into 3 equal parts
np.split(arr, [2,4])       # split before index 2 and before index 4
np.split(A, 2, axis=0)     # split rows
np.split(B, 3, axis=1)     # split columns
```
> Returns a **list** of arrays.

## Broadcasting
NumPy expands a smaller array so it can operate with a larger one element-wise.

**Rules** (compare shapes from the rightmost dimension):
- Dimensions are compatible if they are **equal**, or **one of them is 1**.
- Otherwise → `ValueError`.

```python
A.shape = (2,3)
B.shape = (3,)    → treated as (1,3) → broadcasts to (2,3)   ✔
B.shape = (2,1)   → broadcasts to (2,3)                       ✔
B.shape = (2,2)   → 3 vs 2 mismatch, neither is 1              ✘ error
```

## Vectorization
Perform operations on the whole array at once instead of looping element by element (faster, used heavily in matrix ops).
```python
np.sum(arr)
arr *= 2        # in-place vectorized operation
```

## Handling NaN and Infinite Values
```python
np.isnan(arr)                              # True where value is NaN
np.nan == np.nan                           # always False! (can't compare NaN)
np.nan_to_num(arr, nan=9)                  # replace NaN with a value (default 0)

np.isinf(arr)                              # True where value is +inf/-inf
np.any(np.isinf(arr))                      # check if ANY infinite value exists
np.nan_to_num(arr, posinf=100, neginf=-100)  # replace +inf/-inf with values
```

## Quick Reference: Key Interview Points
- NumPy arrays are faster and use less memory than Python lists — no explicit loops needed for math.
- `reshape()` / `ravel()` return **views** (share memory) — modifying one modifies the other.
- `flatten()` returns a **copy** — original stays unaffected.
- Fancy indexing (`arr[[0,2,4]]`) returns a **copy**, not a view.
- `np.nan == np.nan` → **False**.
- Reverse an array without a loop: `arr[::-1]`.

## Returns a VIEW (shares memory with original)
Basic slicing — arr[0:5], arr[::2], arr[-1::-1], etc.
reshape() — arr.reshape(2,3) (as long as data is contiguous)
ravel() — arr2D.ravel()
Transpose — arr.T
Indexing with a single index that returns a sub-array view along an axis (e.g. arr2d[1] for a row)

Changing the view also changes the original array, since they share the same underlying data buffer.

## Returns a COPY (independent, new memory)
flatten() — arr2D.flatten()
Fancy indexing — arr[[0, 2, 4]]
Boolean masking — arr[arr % 2 == 0]
np.insert(), np.append(), np.delete(), np.concatenate() — all return new arrays, original untouched
np.vstack() / np.hstack() — new array
np.split() — list of new arrays
.astype() — always returns a copy, even if converting to the same dtype
Arithmetic operations — arr + 2, arr * 2, etc. → new array (original unchanged, unless you use +=, *= which are in-place)

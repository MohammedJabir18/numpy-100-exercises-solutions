# 100 NumPy Exercises — Fast-Lookup Cheatsheet

> Quick-reference guide for all 100 NumPy exercises. For deep-dive explanations, intuition, and alternatives, see the respective [Topic Notebooks](../notebooks/).

---

## Table of Contents
- [1. Array Basics & Creation (Ex 01–15)](#1-array-basics--creation-ex-0115)
- [2. Indexing, Slicing & Reshaping (Ex 16–30)](#2-indexing-slicing--reshaping-ex-1630)
- [3. Math, Statistics & Broadcasting (Ex 31–45)](#3-math-statistics--broadcasting-ex-3145)
- [4. Random Sampling, Sorting & Searching (Ex 46–60)](#4-random-sampling-sorting--searching-ex-4660)
- [5. Data Types, Bins & Moving Windows (Ex 61–75)](#5-data-types-bins--moving-windows-ex-6175)
- [6. Linear Algebra & Matrix Operations (Ex 76–85)](#6-linear-algebra--matrix-operations-ex-7685)
- [7. Advanced Vectorization & Einsum (Ex 86–100)](#7-advanced-vectorization--einsum-ex-86100)

---

## 1. Array Basics & Creation (Ex 01–15)

### 01. Import numpy as `np` and print version `★☆☆`
```python
import numpy as np
print(np.__version__)
```

### 02. Print numpy configuration `★☆☆`
```python
np.show_config()
```

### 03. Create a null vector of size 10 `★☆☆`
```python
Z = np.zeros(10)
```

### 04. Find the memory size of an array `★☆☆`
```python
Z = np.zeros((10, 10))
print(f"Memory size: {Z.nbytes} bytes (or {Z.size * Z.itemsize} bytes)")
```

### 05. Get documentation of `np.add` from command line / code `★☆☆`
```python
np.info(np.add)
# Or in shell: python -c "import numpy; numpy.info(numpy.add)"
```

### 06. Create a null vector of size 10 but fifth value is 1 `★☆☆`
```python
Z = np.zeros(10)
Z[4] = 1
```

### 07. Create a vector with values ranging from 10 to 49 `★☆☆`
```python
Z = np.arange(10, 50)
```

### 08. Reverse a vector (first element becomes last) `★☆☆`
```python
Z = np.arange(50)
Z = Z[::-1]  # Or: np.flip(Z)
```

### 09. Create a 3x3 matrix with values ranging from 0 to 8 `★☆☆`
```python
Z = np.arange(9).reshape(3, 3)
```

### 10. Find indices of non-zero elements from `[1, 2, 0, 0, 4, 0]` `★☆☆`
```python
nz = np.nonzero([1, 2, 0, 0, 4, 0])
# Returns: (array([0, 1, 4]),)
```

### 11. Create a 3x3 identity matrix `★☆☆`
```python
Z = np.eye(3)
```

### 12. Create a 3x3x3 array with random values `★☆☆`
```python
rng = np.random.default_rng()
Z = rng.random((3, 3, 3))
```

### 13. Create a 10x10 array with random values and find min and max `★☆☆`
```python
Z = np.random.default_rng().random((10, 10))
zmin, zmax = Z.min(), Z.max()
```

### 14. Create a random vector of size 30 and find the mean value `★☆☆`
```python
Z = np.random.default_rng().random(30)
m = Z.mean()
```

### 15. Create a 2D array with 1 on the border and 0 inside `★☆☆`
```python
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
```

---

## 2. Indexing, Slicing & Reshaping (Ex 16–30)

### 16. Add a border (filled with 0's) around an existing array `★☆☆`
```python
Z = np.ones((5, 5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
```

### 17. Result of expressions with NaN and Inf `★☆☆`
```python
print(0 * np.nan)        # nan
print(np.nan == np.nan)  # False
print(np.inf > np.nan)   # False
print(np.nan - np.nan)   # nan
print(np.nan in set([np.nan])) # True
print(0.3 == 3 * 0.1)    # False (floating point precision)
```

### 18. Create a 5x5 matrix with values 1,2,3,4 just below diagonal `★☆☆`
```python
Z = np.diag(1 + np.arange(4), k=-1)
```

### 19. Create an 8x8 matrix and fill it with a checkerboard pattern `★☆☆`
```python
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
```

### 20. Shape (6,7,8) array: index (x,y,z) of 100th element `★☆☆`
```python
coords = np.unravel_index(99, (6, 7, 8))
# Returns: (1, 5, 3)
```

### 21. Create a checkerboard 8x8 matrix using `np.tile` `★☆☆`
```python
Z = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
```

### 22. Normalize a 5x5 random matrix `★☆☆`
```python
Z = np.random.default_rng().random((5, 5))
Z_norm = (Z - Z.min()) / (Z.max() - Z.min())
```

### 23. Create custom dtype describing RGBA color (4 unsigned bytes) `★☆☆`
```python
color_dtype = np.dtype([("r", np.ubyte),
                        ("g", np.ubyte),
                        ("b", np.ubyte),
                        ("a", np.ubyte)])
```

### 24. Multiply a 5x3 matrix by a 3x2 matrix `★☆☆`
```python
A = np.ones((5, 3))
B = np.ones((3, 2))
Z = A @ B  # Modern Python operator (or np.dot(A, B))
```

### 25. Given 1D array, negate all elements between 3 and 8 in place `★☆☆`
```python
Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
```

### 26. Output of `sum(range(5), -1)` vs `np.sum(range(5), -1)` `★★☆`
```python
print(sum(range(5), -1))    # 9  (built-in sum starts with initial value -1: 0+1+2+3+4 + (-1))
print(np.sum(range(5), -1)) # 10 (np.sum treats second arg as axis=-1)
```

### 27. Legal expressions with integer vector Z `★☆☆`
```python
Z = np.arange(5)
# Legal:
_ = Z**Z
_ = 2 << Z >> 2
_ = Z < -Z
_ = 1j * Z
_ = Z / 1 / 1
# Illegal:
# Z < Z > Z (ValueError: truth value of an array is ambiguous)
```

### 28. Result of floating point comparison expressions `★☆☆`
```python
print(np.array(0) / np.array(0))                # nan (with warning)
print(np.array(0) // np.array(0))               # 0 (with warning)
print(np.array([np.nan]).astype(int).astype(float)) # Implementation-dependent int cast
```

### 29. How to round away from zero a float array `★★☆`
```python
Z = np.random.default_rng().uniform(-10, 10, 10)
Z_rounded = np.copysign(np.ceil(np.abs(Z)), Z)
```

### 30. How to find common values between two arrays `★☆☆`
```python
Z1 = np.random.default_rng().integers(0, 10, 10)
Z2 = np.random.default_rng().integers(0, 10, 10)
common = np.intersect1d(Z1, Z2)
```

---

## 3. Math, Statistics & Broadcasting (Ex 31–45)

### 31. How to ignore all numpy warnings `★☆☆`
```python
# Context manager (best practice):
with np.errstate(all="ignore"):
    _ = np.ones(1) / 0
```

### 32. Is `np.sqrt(-1) == np.emath.sqrt(-1)` true? `★☆☆`
```python
# False! np.sqrt(-1) yields nan, np.emath.sqrt(-1) yields 1j
print(np.sqrt(-1) == np.emath.sqrt(-1))  # False (nan != 1j)
```

### 33. Get dates of yesterday, today, and tomorrow `★☆☆`
```python
today     = np.datetime64('today', 'D')
yesterday = today - np.timedelta64(1, 'D')
tomorrow  = today + np.timedelta64(1, 'D')
```

### 34. Get all dates corresponding to month of July 2016 `★★☆`
```python
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
```

### 35. Compute `((A+B)*(-A/2))` in place without copy `★★☆`
```python
A = np.ones(3) * 1
B = np.ones(3) * 2
np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
np.multiply(A, B, out=A)
```

### 36. Extract integer part of float array using 4 methods `★★☆`
```python
Z = np.random.default_rng().uniform(0, 10, 10)
print(Z - Z % 1)
print(Z // 1)
print(np.floor(Z))
print(Z.astype(int))
print(np.trunc(Z))
```

### 37. Create a 5x5 matrix with row values ranging from 0 to 4 `★☆☆`
```python
Z = np.zeros((5, 5)) + np.arange(5)
```

### 38. Build array from a generator yielding 10 integers `★☆☆`
```python
def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(), dtype=float, count=10)
```

### 39. Create vector of size 10 from 0 to 1, both excluded `★☆☆`
```python
Z = np.linspace(0, 1, 11, endpoint=False)[1:]
```

### 40. Create a random vector of size 10 and sort it `★☆☆`
```python
Z = np.random.default_rng().random(10)
Z.sort()
```

### 41. Sum a small array faster than `np.sum` `★★☆`
```python
Z = np.arange(10)
total = np.add.reduce(Z)  # Reduces overhead vs np.sum wrapper
```

### 42. Check if two random arrays A and B are equal `★★☆`
```python
A = np.random.default_rng().integers(0, 2, 5)
B = np.random.default_rng().integers(0, 2, 5)
equal = np.array_equal(A, B)      # Strict exact equality
close = np.allclose(A, B)        # Tolerance-based for floats
```

### 43. Make an array immutable (read-only) `★★☆`
```python
Z = np.zeros(10)
Z.flags.writeable = False
```

### 44. Convert 10x2 cartesian coordinates to polar coordinates `★★☆`
```python
Z = np.random.default_rng().random((10, 2))
X, Y = Z[:, 0], Z[:, 1]
R = np.hypot(X, Y)
T = np.arctan2(Y, X)
```

### 45. Create random vector size 10 and replace max value with 0 `★☆☆`
```python
Z = np.random.default_rng().random(10)
Z[Z.argmax()] = 0
```

---

## 4. Random Sampling, Sorting & Searching (Ex 46–60)

### 46. Structured array with x, y coordinates covering [0,1]x[0,1] `★★☆`
```python
Z = np.zeros((5, 5), [('x', float), ('y', float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0, 1, 5), np.linspace(0, 1, 5))
```

### 47. Given two arrays X and Y, construct Cauchy matrix C `★★☆`
```python
X = np.arange(8)
Y = X + 0.5
C = 1.0 / np.subtract.outer(X, Y)
```

### 48. Print min and max representable values for scalar dtypes `★★☆`
```python
for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min, np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min, np.finfo(dtype).max, np.finfo(dtype).eps)
```

### 49. How to print all values of an array without truncation `★☆☆`
```python
np.set_printoptions(threshold=np.inf)
Z = np.zeros((16, 16))
# print(Z)
```

### 50. How to find closest value (to given scalar) in a vector `★☆☆`
```python
Z = np.arange(100)
v = 42.4
idx = (np.abs(Z - v)).argmin()
print(Z[idx])
```

### 51. Structured array representing position (x,y) and color (r,g,b) `★★☆`
```python
Z = np.zeros(10, [('position', [('x', float), ('y', float)]),
                  ('color',    [('r', float), ('g', float), ('b', float)])])
```

### 52. Point-by-point distances in shape (100, 2) array `★★☆`
```python
Z = np.random.default_rng().random((100, 2))
D = np.hypot(Z[:, 0, None] - Z[:, 0], Z[:, 1, None] - Z[:, 1])
```

### 53. Convert float32 array into int32 in place `★★☆`
```python
Z = (np.random.default_rng().random(10) * 100).astype(np.float32)
Y = Z.view(np.int32)
Y[:] = Z
```

### 54. How to read file with genfromtxt `★☆☆`
```python
from io import StringIO
s = StringIO("""1, 2, 3, 4, 5\n6,  ,  , 7, 8\n ,  , 9,10,11\n""")
Z = np.genfromtxt(s, delimiter=",", dtype=np.float64)
```

### 55. What is equivalent of enumerate for numpy arrays `★☆☆`
```python
Z = np.arange(9).reshape(3, 3)
for index, value in np.ndenumerate(Z):
    pass
for index in np.ndindex(Z.shape):
    pass
```

### 56. Generate a generic 2D Gaussian-like array `★★☆`
```python
X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
D = np.hypot(X, Y)
sigma, mu = 1.0, 0.0
G = np.exp(-((D - mu) ** 2 / (2.0 * sigma ** 2)))
```

### 57. Randomly place p elements in a 2D array `★★☆`
```python
n, p = 10, 3
Z = np.zeros((n, n))
np.put(Z, np.random.default_rng().choice(range(n * n), p, replace=False), 1)
```

### 58. Subtract mean of each row of a matrix `★★☆`
```python
X = np.random.default_rng().random((5, 10))
Y = X - X.mean(axis=1, keepdims=True)
```

### 59. How to sort an array by the nth column `★★☆`
```python
Z = np.random.default_rng().integers(0, 10, (3, 3))
Z_sorted = Z[Z[:, 1].argsort()]  # Sorted by column 1
```

### 60. How to tell if a given 2D array has null columns `★★☆`
```python
Z = np.random.default_rng().integers(0, 3, (3, 10))
print((~Z.any(axis=0)).any())
```

---

## 5. Data Types, Bins & Moving Windows (Ex 61–75)

### 61. Find nearest value from given target in an array `★★☆`
```python
Z = np.random.default_rng().uniform(0, 1, 10)
z = 0.5
nearest = Z.flat[np.abs(Z - z).argmin()]
```

### 62. Sum (1,3) and (3,1) arrays using `nditer` `★★☆`
```python
A = np.arange(3).reshape(3, 1)
B = np.arange(3).reshape(1, 3)
it = np.nditer([A, B, None])
for x, y, z in it:
    z[...] = x + y
res = it.operands[2]
```

### 63. Create an array class that has a name attribute `★★☆`
```python
class NamedArray(np.ndarray):
    def __new__(cls, array, name="no_name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__(self, obj):
        if obj is None: return
        self.name = getattr(obj, 'name', "no_name")
```

### 64. Add 1 to elements indexed by another vector (handling duplicates) `★★☆`
```python
Z = np.zeros(10)
I = np.random.default_rng().integers(0, len(Z), 20)
np.add.at(Z, I, 1)
```

### 65. Accumulate vector elements based on index list `★★☆`
```python
X = [1, 2, 3, 4, 5, 6]
I = [1, 3, 9, 3, 4, 1]
F = np.bincount(I, weights=X)
```

### 66. Compute number of unique colors in a (w,h,3) image `★★☆`
```python
w, h = 16, 16
I = np.random.default_rng().integers(0, 2, (h, w, 3), dtype=np.ubyte)
n_unique = len(np.unique(I.reshape(-1, 3), axis=0))
```

### 67. Sum over the last two axes of a 4D array at once `★★☆`
```python
A = np.random.default_rng().integers(0, 10, (3, 4, 3, 4))
res = A.sum(axis=(-2, -1))
```

### 68. Compute means of subsets defined by category array `★★☆`
```python
D = np.random.default_rng().uniform(0, 1, 100)
S = np.random.default_rng().integers(0, 10, 100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
```

### 69. Get diagonal of dot product efficiently `★★☆`
```python
A = np.random.default_rng().uniform(0, 1, (5, 5))
B = np.random.default_rng().uniform(0, 1, (5, 5))
diag_dot = np.sum(A * B.T, axis=1)  # O(N^2) instead of O(N^3)
```

### 70. Interleave 3 consecutive zeros between vector values `★★☆`
```python
Z = np.array([1, 2, 3, 4, 5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z) - 1) * nz)
Z0[::nz + 1] = Z
```

### 71. Multiply (5,5,3) array by (5,5) array `★★☆`
```python
A = np.ones((5, 5, 3))
B = 2 * np.ones((5, 5))
res = A * B[:, :, None]
```

### 72. Swap two rows of an array `★★☆`
```python
A = np.arange(25).reshape(5, 5)
A[[0, 1]] = A[[1, 0]]
```

### 73. Unique line segments from set of triangles `★★★`
```python
faces = np.random.default_rng().integers(0, 100, (10, 3))
F = np.roll(faces.repeat(2, axis=1), -1, axis=1)
F = F.reshape(len(F) * 3, 2)
F = np.sort(F, axis=1)
G = F.view(dtype=[('p0', F.dtype), ('p1', F.dtype)])
unique_edges = np.unique(G)
```

### 74. Invert `bincount` to produce source array `★★☆`
```python
C = np.bincount([1, 1, 2, 3, 4, 4, 6])
A = np.repeat(np.arange(len(C)), C)
```

### 75. Sliding window average over array `★★★`
```python
def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
```

---

## 6. Linear Algebra & Matrix Operations (Ex 76–85)

### 76. Sliding 2D window matrix using stride tricks `★★★`
```python
from numpy.lib.stride_tricks import sliding_window_view
Z = np.arange(10)
windows = sliding_window_view(Z, window_shape=3)
```

### 77. In-place boolean negation / sign inversion `★★☆`
```python
# Boolean:
Z = np.random.default_rng().integers(0, 2, 10, dtype=bool)
np.logical_not(Z, out=Z)
# Float sign inversion:
F = np.random.default_rng().uniform(-1, 1, 10)
np.negative(F, out=F)
```

### 78. Distance from point p to 2D lines `★★★`
```python
def distance(P0, P1, p):
    T = P1 - P0
    L = (T**2).sum(axis=1)
    u = -((P0[:, 0] - p[0]) * T[:, 0] + (P0[:, 1] - p[1]) * T[:, 1]) / L
    u = u.reshape(len(u), 1)
    d = P0 + u * T - p
    return np.sqrt((d**2).sum(axis=1))
```

### 79. Distance from points to lines `★★★`
```python
P0 = np.random.default_rng().uniform(-10, 10, (10, 2))
P1 = np.random.default_rng().uniform(-10, 10, (10, 2))
p  = np.random.default_rng().uniform(-10, 10, (10, 2))
# Evaluates distances for each point p[i] to line (P0[i], P1[i])
```

### 80. Centered subpart extraction with fill `★★★`
```python
Z = np.ones((5, 5))
# Use np.pad and slice around center coordinate
```

### 81. Rolling sub-arrays generation `★★☆`
```python
Z = np.arange(1, 15)
R = sliding_window_view(Z, window_shape=4)
```

### 82. Compute matrix rank `★★☆`
```python
Z = np.random.default_rng().uniform(0, 1, (10, 10))
rank = np.linalg.matrix_rank(Z)
```

### 83. Find most frequent value in array `★★☆`
```python
Z = np.random.default_rng().integers(0, 10, 50)
most_frequent = np.bincount(Z).argmax()
```

### 84. Extract contiguous 3x3 blocks from 10x10 matrix `★★☆`
```python
Z = np.random.default_rng().integers(0, 5, (10, 10))
blocks = sliding_window_view(Z, window_shape=(3, 3))
```

### 85. Symmetric 2D array subclass `★★★`
```python
class SymArray(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super().__setitem__((i, j), value)
        super().__setitem__((j, i), value)
```

---

## 7. Advanced Vectorization & Einsum (Ex 86–100)

### 86. Sum of p matrix products at once using einsum `★★★`
```python
p, n = 10, 5
M = np.ones((p, n, n))
V = np.ones((p, n, 1))
S = np.einsum('ijk,ikl->jl', M, V)
```

### 87. Block-sum of 16x16 array with 4x4 blocks `★★☆`
```python
Z = np.ones((16, 16))
block_sum = Z.reshape(4, 4, 4, 4).sum(axis=(1, 3))
```

### 88. Conway's Game of Life vectorized implementation `★★★`
```python
def iterate_life(Z):
    # Count 8 neighbors using 2D slicing
    N = (Z[0:-2, 0:-2] + Z[0:-2, 1:-1] + Z[0:-2, 2:] +
         Z[1:-1, 0:-2]                 + Z[1:-1, 2:] +
         Z[2:  , 0:-2] + Z[2:  , 1:-1] + Z[2:  , 2:])
    birth = (N == 3) & (Z[1:-1, 1:-1] == 0)
    survive = ((N == 2) | (N == 3)) & (Z[1:-1, 1:-1] == 1)
    Z[...] = 0
    Z[1:-1, 1:-1][birth | survive] = 1
    return Z
```

### 89. Get n largest values of an array `★★☆`
```python
Z = np.arange(10000)
np.random.default_rng().shuffle(Z)
n = 5
top_n = Z[np.argpartition(-Z, n)[:n]]
```

### 90. Cartesian product of arbitrary vectors `★★★`
```python
def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)
    ix = np.indices(shape, dtype=int)
    ix = ix.reshape(len(arrays), -1).T
    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix[:, n]]
    return ix
```

### 91. Create record array from regular array `★☆☆`
```python
Z = np.array([("A", 2.5, 3), ("B", 3.6, 2)], dtype=[('x', 'U10'), ('y', float), ('z', int)])
R = np.rec.array(Z)
```

### 92. Large vector $Z^3$ computed with 3 methods `★★★`
```python
Z = np.random.default_rng().random(int(1e6))
# Method 1:
_ = np.power(Z, 3)
# Method 2:
_ = Z * Z * Z
# Method 3:
_ = np.einsum('i,i,i->i', Z, Z, Z)
```

### 93. Rows containing elements of another array `★★★`
```python
A = np.random.default_rng().integers(0, 5, (8, 3))
B = np.random.default_rng().integers(0, 5, (2, 2))
C = (A[..., np.newaxis, np.newaxis] == B)
rows = np.where(C.any((3, 1)).all(1))[0]
```

### 94. Extract rows with unequal values from 10x3 matrix `★★☆`
```python
Z = np.random.default_rng().integers(0, 5, (10, 3))
unequal_rows = Z[~np.all(Z[:, 1:] == Z[:, :-1], axis=1)]
```

### 95. Convert integer vector to binary matrix `★★☆`
```python
I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
binary_matrix = np.unpackbits(I[:, np.newaxis], axis=1)
```

### 96. Extract unique rows from 2D array `★★☆`
```python
Z = np.random.default_rng().integers(0, 2, (6, 3))
unique_rows = np.unique(Z, axis=0)
```

### 97. `np.einsum` equivalent for inner, outer, sum, and mul `★★☆`
```python
A = np.arange(3)
B = np.arange(3)
inner_prod = np.einsum('i,i->', A, B)
outer_prod = np.einsum('i,j->ij', A, B)
sum_vals   = np.einsum('i->', A)
mul_vals   = np.einsum('i,i->i', A, B)
```

### 98. Equidistant sampling of a 2D curve path `★★★`
```python
phi = np.arange(0, 10 * np.pi, 0.1)
a = 1
x = a * phi * np.cos(phi)
y = a * phi * np.sin(phi)
dr = np.hypot(np.diff(x), np.diff(y))
d = np.cumsum(dr)
```

### 99. Select rows from multinomial distribution `★★★`
```python
X = np.random.default_rng().integers(0, 5, (10, 3))
n = 4
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M &= (X.sum(axis=-1) == n)
```

### 100. Bootstrapped 95% confidence interval for mean `★★★`
```python
X = np.random.default_rng().normal(0, 1, 100)
n_boot = 1000
idx = np.random.default_rng().integers(0, len(X), (n_boot, len(X)))
means = X[idx].mean(axis=1)
conf_int = np.percentile(means, [2.5, 97.5])
```

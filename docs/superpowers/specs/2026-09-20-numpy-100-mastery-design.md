# Design Document: NumPy 100 Mastery

- **Date:** 2026-09-20
- **Project Name:** `numpy-100-mastery` (Repository: `numpy-100-exercises-solutions`)
- **Status:** Approved by User

---

## 1. Overview & Objective

This project creates an educational, modern, and comprehensive GitHub repository based on the famous **100 NumPy Exercises** challenge (originally curated by Nicolas P. Rougier) and popularized by Keith Galli's video tutorial (*"Solving 100 Python NumPy Problems! (From easy to difficult)"*).

Rather than presenting bare one-line answers, this repository provides:
- **7 topic-focused Jupyter Notebooks** grouping related exercises logically.
- **Detailed educational breakdowns** for every single exercise (Intuition, Primary Modern NumPy 2.x Solution, Alternatives, Gotchas/Takeaways).
- **A fast-lookup searchable Cheatsheet** in Markdown for instant reference.
- **A modern, badge-rich README** with clickable index, progress checkboxes, difficulty tags, and environment setup instructions.

---

## 2. Directory Architecture

```text
numpy-100-exercises-solutions/
├── README.md                                    # Master hub: index table, progress tracker, badges, video credit
├── LICENSE                                      # MIT License
├── requirements.txt                             # NumPy >= 2.0, Jupyter, Matplotlib, etc.
├── .gitignore                                   # Standard Python, Jupyter (.ipynb_checkpoints), virtualenv, OS
├── notebooks/
│   ├── 01_array_creation_and_basics.ipynb       # Exercises 01–15 (Import, creation, memory, attributes)
│   ├── 02_indexing_slicing_and_reshaping.ipynb  # Exercises 16–30 (Padding, strides, diagonals, reshape)
│   ├── 03_math_statistics_and_broadcasting.ipynb# Exercises 31–45 (Matrix ops, broadcasting, rounding)
│   ├── 04_random_sampling_and_sorting.ipynb     # Exercises 46–60 (RNG, seeds, distributions, argsort)
│   ├── 05_dtypes_and_structured_arrays.ipynb    # Exercises 61–75 (Custom dtypes, records, datetimes)
│   ├── 06_linear_algebra_and_matrix_ops.ipynb   # Exercises 76–85 (Norms, eigenvalues, SVD, solve)
│   └── 07_advanced_vectorization_and_einsum.ipynb# Exercises 86–100 (Stride tricks, einsum, memory layout)
├── cheatsheets/
│   └── all_100_solutions.md                     # Markdown fast-lookup table of all 100 exercises & solutions
└── assets/
    └── banner.svg                               # Clean SVG banner for README
```

---

## 3. Exercise Structure Specification

Each exercise in every notebook follows this standardized layout:

```markdown
### Exercise {XX}: {Title}
**Difficulty:** `★☆☆` | `★★☆` | `★★★`  
**Tags:** `{e.g., Array Creation, Memory, Slicing}`

#### 💡 Intuition & Concept
Brief explanation of what NumPy does behind the scenes and the relevant API concepts.

#### 🛠️ Solution
```python
# Modern, idiomatic NumPy code
```

#### 🔄 Alternative / Benchmark
Secondary approach (e.g. comparing `np.pad` vs slice assignment, or vectorized vs loop), showing performance or flexibility trade-offs.

#### ⚠️ Key Takeaway & Common Pitfalls
Gotchas to avoid (e.g., shallow views vs deep copies, integer division, dtype overflow).
```

---

## 4. Notebook Breakdown (The 100 Exercises)

### Notebook 1: `01_array_creation_and_basics.ipynb` (Ex 1–15)
- **Ex 01:** Import numpy as `np` and check version
- **Ex 02:** Print numpy configuration
- **Ex 03:** Create a null vector of size 10
- **Ex 04:** Find the memory size of an array (`nbytes` vs `size * itemsize`)
- **Ex 05:** Get documentation of `np.add` from CLI / Python help
- **Ex 06:** Create null vector of size 10 with 5th value equal to 1
- **Ex 07:** Create vector with values ranging from 10 to 49
- **Ex 08:** Reverse a vector (`[::-1]`, `np.flip`)
- **Ex 09:** Create a 3x3 matrix with values ranging from 0 to 8
- **Ex 10:** Find indices of non-zero elements (`np.nonzero`)
- **Ex 11:** Create a 3x3 identity matrix (`np.eye`, `np.identity`)
- **Ex 12:** Create a 3x3x3 array with random values
- **Ex 13:** Create a 10x10 array with random values and find min and max
- **Ex 14:** Create a random vector of size 30 and find mean value
- **Ex 15:** Create a 2D array with 1 on the border and 0 inside

### Notebook 2: `02_indexing_slicing_and_reshaping.ipynb` (Ex 16–30)
- **Ex 16:** Add a border (0s) around an existing array (`np.pad` vs slice)
- **Ex 17:** Result of NaN/Inf arithmetic expressions
- **Ex 18:** Create a 5x5 matrix with values 1,2,3,4 just below diagonal (`np.diag`)
- **Ex 19:** Create an 8x8 matrix with a checkerboard pattern
- **Ex 20:** Shape (6,7,8) array: index (x,y,z) of 100th element (`np.unravel_index`)
- **Ex 21:** Create checkerboard 8x8 matrix using `np.tile`
- **Ex 22:** Normalize a 5x5 random matrix (`(x - min)/(max - min)`)
- **Ex 23:** Create custom dtype for RGBA color (4 unsigned bytes)
- **Ex 24:** Multiply a 5x3 matrix by a 3x2 matrix (`@`, `np.dot`)
- **Ex 25:** Given a 1D array, negate all elements between 3 and 8 in place
- **Ex 26:** Behavior of Python `sum` vs `np.sum` with negative start/axis
- **Ex 27:** Legal expressions with integer vectors (`Z**Z`, `2 << Z >> 2`, etc.)
- **Ex 28:** Floating point arithmetic and comparisons (`np.nan in set`, etc.)
- **Ex 29:** Round away from zero for float arrays (`np.copysign`, `np.ceil`)
- **Ex 30:** Find common values between two arrays (`np.intersect1d`)

### Notebook 3: `03_math_statistics_and_broadcasting.ipynb` (Ex 31–45)
- **Ex 31:** Ignore all numpy warnings (and context manager best practice)
- **Ex 32:** `np.sqrt(-1) == np.emath.sqrt(-1)` comparison
- **Ex 33:** Get dates of yesterday, today, and tomorrow (`np.datetime64`)
- **Ex 34:** Get all dates in month of July 2016 (`np.arange` with `datetime64[D]`)
- **Ex 35:** Compute `((A+B)*(-A/2))` in place without copying
- **Ex 36:** Extract integer part of float array using 4 methods
- **Ex 37:** Create a 5x5 matrix with row values ranging from 0 to 4 (`np.zeros + np.arange`)
- **Ex 38:** Build array from a generator yielding 10 integers (`np.fromiter`)
- **Ex 39:** Vector of size 10 from 0 to 1, both excluded (`np.linspace`)
- **Ex 40:** Create random vector of size 10 and sort it (`np.sort`)
- **Ex 41:** Sum small array faster than `np.sum` (`np.add.reduce`)
- **Ex 42:** Compare two random arrays for equality (`np.array_equal`, `np.allclose`)
- **Ex 43:** Make an array immutable / read-only (`flags.writeable = False`)
- **Ex 44:** Convert 10x2 cartesian coordinates to polar coordinates
- **Ex 45:** Replace maximum value in a vector with 0 (`arr.argmax()`)

### Notebook 4: `04_random_sampling_and_sorting.ipynb` (Ex 46–60)
- **Ex 46:** Create structured array with x, y coordinates covering [0,1]x[0,1]
- **Ex 47:** Construct Cauchy matrix from X and Y (`1.0 / (X - Y)`)
- **Ex 48:** Print min and max representable values for scalar dtypes (`np.iinfo`, `np.finfo`)
- **Ex 49:** Print all elements of array without truncation (`np.set_printoptions`)
- **Ex 50:** Find closest value to given scalar in a vector
- **Ex 51:** Structured array with position (x,y) and color (r,g,b)
- **Ex 52:** Point-by-point distances in (100,2) coordinates (`scipy.spatial` / broadcasting)
- **Ex 53:** Convert float32 array to int32 in place (`view` vs astype)
- **Ex 54:** Read structured data from text / string (`np.genfromtxt`)
- **Ex 55:** Enumerate for numpy arrays (`np.ndenumerate`, `np.ndindex`)
- **Ex 56:** Generate 2D Gaussian-like array
- **Ex 57:** Randomly place p elements in a 2D array (`np.put`, `np.random.choice`)
- **Ex 58:** Subtract mean of each row of a matrix (`arr - arr.mean(axis=1, keepdims=True)`)
- **Ex 59:** Sort array by the nth column (`arr[arr[:, n].argsort()]`)
- **Ex 60:** Check if 2D array has null / all-zero columns

### Notebook 5: `05_dtypes_and_structured_arrays.ipynb` (Ex 61–75)
- **Ex 61:** Find nearest value from given target in an array
- **Ex 62:** Sum (1,3) and (3,1) using `np.nditer`
- **Ex 63:** Subclass `np.ndarray` to add a `.name` attribute
- **Ex 64:** Add 1 to elements indexed by another vector (handling duplicates: `np.add.at`)
- **Ex 65:** Accumulate vector elements based on index list (`np.bincount`)
- **Ex 66:** Compute number of unique colors in a (w,h,3) image
- **Ex 67:** Sum over the last two axes of a 4D array at once
- **Ex 68:** Compute means of subsets defined by category array
- **Ex 69:** Get diagonal of a dot product efficiently (`np.sum(A * B.T, axis=1)`)
- **Ex 70:** Interleave 3 consecutive zeros between vector values
- **Ex 71:** Multiply (5,5,3) array by (5,5) array using broadcasting
- **Ex 72:** Swap two rows of an array in place
- **Ex 73:** Find unique line segments from set of 10 triangles
- **Ex 74:** Reconstruct array A from its bincount array C (`np.repeat`)
- **Ex 75:** Moving average / sliding window using `np.convolve` / `lib.stride_tricks`

### Notebook 6: `06_linear_algebra_and_matrix_ops.ipynb` (Ex 76–85)
- **Ex 76:** Sliding 2D window matrix using `np.lib.stride_tricks.sliding_window_view`
- **Ex 77:** In-place boolean negation / sign inversion (`np.logical_not`, `np.negative`)
- **Ex 78:** Compute distances from point p to 2D lines defined by (P0, P1)
- **Ex 79:** Distance from set of points P to set of lines (P0, P1)
- **Ex 80:** Extract fixed subpart centered on an element with border fill
- **Ex 81:** Rolling sub-arrays generation
- **Ex 82:** Compute matrix rank (`np.linalg.matrix_rank`)
- **Ex 83:** Find most frequent value in array (`np.bincount.argmax`)
- **Ex 84:** Extract contiguous 3x3 blocks from 10x10 matrix
- **Ex 85:** Symmetric 2D array subclass where `Z[i,j] == Z[j,i]`

### Notebook 7: `07_advanced_vectorization_and_einsum.ipynb` (Ex 86–100)
- **Ex 86:** Sum of p matrix products at once using `np.einsum`
- **Ex 87:** Block-sum of 16x16 array with 4x4 blocks
- **Ex 88:** Conway's Game of Life vectorized implementation
- **Ex 89:** Get n largest values of an array (`np.argpartition`)
- **Ex 90:** Cartesian product of arbitrary vectors
- **Ex 91:** Create record array from regular array (`np.core.records.fromarrays`)
- **Ex 92:** Large vector $Z^3$ computed with 3 methods & performance benchmark
- **Ex 93:** Find rows in A containing elements of B regardless of order
- **Ex 94:** Extract rows with unequal values from 10x3 matrix
- **Ex 95:** Convert integer vector to binary matrix representation
- **Ex 96:** Extract unique rows from 2D array (`np.unique(..., axis=0)`)
- **Ex 97:** `np.einsum` equivalent for inner, outer, sum, and mul
- **Ex 98:** Equidistant sampling of a 2D curve path
- **Ex 99:** Select rows corresponding to draws from multinomial distribution
- **Ex 100:** Bootstrapped 95% confidence interval for 1D array mean

---

## 5. Verification & Testing

- Every solution verified against NumPy 2.x compatibility.
- Ensure Jupyter notebooks can execute cleanly from top to bottom.
- Provide a validation script to test all exercises programmatically.

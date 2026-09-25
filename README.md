<div align="center">

![NumPy 100 Mastery Banner](assets/banner.svg)

# 🚀 100 NumPy Challenge: My Learning Journey & Practice Template

**A public, hands-on challenge repository tracking my journey through the famous 100 NumPy exercises — designed for my own manual practice and as a reference template for other learners.**

[![Author](https://img.shields.io/badge/Challenger-Mohammed%20Jabir-0284C7?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MohammedJabir18)
[![Challenge Status](https://img.shields.io/badge/Challenge-In%20Progress-F59E0B?style=for-the-badge&logo=target&logoColor=white)](notebooks/)
[![Progress](https://img.shields.io/badge/Progress-20%20%2F%20100%20Solved-38BDF8?style=for-the-badge)](notebooks/)
[![NumPy 2.x](https://img.shields.io/badge/numpy-2.x%20Ready-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

[About This Challenge](#-about-this-challenge) • [For Other Learners](#-how-other-learners-can-use-this-repo) • [Quick Start](#-quick-start) • [The 7 Notebooks](#-the-7-practice-notebooks) • [My Progress Tracker](#-master-progress-tracker--checklist) • [Reference Solutions](solutions/reference_solutions.md)

</div>

---

## 🎯 About This Challenge

Welcome! I created this repository as a public commitment to manually tackle and master the famous **[100 numpy exercises](https://github.com/rougier/numpy-100)** curated by Nicolas P. Rougier, inspired by Keith Galli's video walkthrough **["Solving 100 Python NumPy Problems! (From easy to difficult)"](https://www.youtube.com/watch?v=PM504XhEVCU)**.

### 🥊 My Challenge Rules:
1. **Solve Manually First:** Every single exercise is written and solved from scratch in the notebooks without copying pre-written solutions.
2. **Modern NumPy 2.x Practices:** Emphasize modern idioms (e.g. `@` matrix multiplication, `np.lib.stride_tricks.sliding_window_view`, `default_rng()`, vectorized logic).
3. **Deep Understanding over Quick Answers:** Understand the underlying mechanics—memory layout (`nbytes`, strides), broadcasting rules, and avoiding unnecessary copies.
4. **Public Progress:** Continuously commit and check off challenges in the tracker below as I complete them.

```text
Current Progress: [████░░░░░░░░░░░░░░░░] 20 / 100 Solved (20%)
```

---

## 🤝 How Other Learners Can Use This Repo

If you are learning NumPy, data science, or scientific computing in Python, this repository is built to help you too! Here is how you can use it:

### 1. 🍴 Fork or Clone as Your Own Practice Template
You can fork or clone this repository to start your own 100-problem challenge:
```bash
git clone https://github.com/MohammedJabir18/numpy-100-exercises-solutions.git
cd numpy-100-exercises-solutions
```
All notebooks in `notebooks/` come with **clean, empty coding cells**, challenge instructions, difficulty ratings, and expected outputs.

### 2. 💡 Collapsible Dropdown Hints
Stuck on an exercise? Each problem includes a closed `<details><summary>💡 Hint</summary></details>` section. You can try solving it independently, and only expand the hint if you need a conceptual nudge.

### 3. 🔍 Cross-Check Your Work
Once you've written your solution in the notebook, you can compare your approach with the [Reference Solutions](solutions/reference_solutions.md) to discover alternative methods, performance trade-offs, and common pitfalls.

### 4. 💬 Share & Discuss
If you discover a faster, cleaner, or more elegant NumPy one-liner for any challenge, feel free to open an **Issue** or submit a **Pull Request**!

---

## ⚡ Quick Start

### 1. Set Up Environment
```bash
# Clone the repository
git clone https://github.com/MohammedJabir18/numpy-100-exercises-solutions.git
cd numpy-100-exercises-solutions

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Launch JupyterLab
```bash
jupyter lab
```
Open [`notebooks/01_array_creation_and_basics.ipynb`](notebooks/01_array_creation_and_basics.ipynb) and start coding!

---

## 📚 The 7 Practice Notebooks

All 100 challenges are split into 7 progressive topics:

| # | Practice Notebook | Exercises | Status | Difficulty | Core Topics |
|---|---|:---:|:---:|:---:|---|
| **01** | [01. Array Basics & Creation](notebooks/01_array_creation_and_basics.ipynb) | 01–15 | ✅ **15 / 15** | `★☆☆` | Array creation, `nbytes`, memory size, zeros/ones, slicing reversal |
| **02** | [02. Indexing, Slicing & Reshaping](notebooks/02_indexing_slicing_and_reshaping.ipynb) | 16–30 | ⏳ **5 / 15** | `★☆☆` - `★★☆` | `np.pad`, IEEE-754 NaNs, checkerboards, unraveling coordinates, custom RGBA dtypes |
| **03** | [03. Math, Statistics & Broadcasting](notebooks/03_math_statistics_and_broadcasting.ipynb) | 31–45 | ⏳ **0 / 15** | `★☆☆` - `★★☆` | `datetime64` calendars, in-place arithmetic (`out=`), generators, polar coordinates |
| **04** | [04. Random Sampling, Sorting & Searching](notebooks/04_random_sampling_and_sorting.ipynb) | 46–60 | ⏳ **0 / 15** | `★☆☆` - `★★☆` | PRNG distributions, Cauchy matrix, dtype limits, pairwise Euclidean distance, `argsort` |
| **05** | [05. Data Types, Bins & Moving Windows](notebooks/05_dtypes_and_structured_arrays.ipynb) | 61–75 | ⏳ **0 / 15** | `★★☆` - `★★★` | Array subclassing, `np.add.at` accumulation, bincount groupby, moving averages |
| **06** | [06. Linear Algebra & Matrix Operations](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | 76–85 | ⏳ **0 / 10** | `★★☆` - `★★★` | `sliding_window_view`, vector line projections, matrix rank, symmetric matrices |
| **07** | [07. Advanced Vectorization & Einsum](notebooks/07_advanced_vectorization_and_einsum.ipynb) | 86–100 | ⏳ **0 / 15** | `★★☆` - `★★★` | Multi-batch `einsum`, Conway's Game of Life, Cartesian products, bootstrap CI |

---

## 📋 Master Progress Tracker & Checklist

<details open>
<summary><b>Click to expand / collapse all 100 exercises</b></summary>

| # | Status | Exercise Title | Practice Notebook | Diff | Reference Solution |
|:---:|:---:|---|---|:---:|:---:|
| **01** | [x] | Import numpy as `np` and print version | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#01-import-numpy-as-np-and-print-version-) |
| **02** | [x] | Print numpy configuration | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#02-print-numpy-configuration-) |
| **03** | [x] | Create a null vector of size 10 | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#03-create-a-null-vector-of-size-10-) |
| **04** | [x] | Find the memory size of any array | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#04-find-the-memory-size-of-an-array-) |
| **05** | [x] | Get documentation of numpy add function | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#05-get-documentation-of-npadd-from-command-line--code-) |
| **06** | [x] | Create null vector of size 10 but fifth value is 1 | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#06-create-a-null-vector-of-size-10-but-fifth-value-is-1-) |
| **07** | [x] | Create vector with values ranging from 10 to 49 | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#07-create-a-vector-with-values-ranging-from-10-to-49-) |
| **08** | [x] | Reverse a vector (first element becomes last) | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#08-reverse-a-vector-first-element-becomes-last-) |
| **09** | [x] | Create 3x3 matrix with values ranging from 0 to 8 | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#09-create-a-3x3-matrix-with-values-ranging-from-0-to-8-) |
| **10** | [x] | Find indices of non-zero elements from `[1,2,0,0,4,0]` | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#10-find-indices-of-non-zero-elements-from-1-2-0-0-4-0-) |
| **11** | [x] | Create a 3x3 identity matrix | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#11-create-a-3x3-identity-matrix-) |
| **12** | [x] | Create a 3x3x3 array with random values | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#12-create-a-3x3x3-array-with-random-values-) |
| **13** | [x] | Create a 10x10 array with random values and find min/max | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#13-create-a-10x10-array-with-random-values-and-find-min-and-max-) |
| **14** | [x] | Create a random vector of size 30 and find mean value | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#14-create-a-random-vector-of-size-30-and-find-the-mean-value-) |
| **15** | [x] | Create a 2D array with 1 on border and 0 inside | [01_basics.ipynb](notebooks/01_array_creation_and_basics.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#15-create-a-2d-array-with-1-on-the-border-and-0-inside-) |
| **16** | [x] | Add a border (filled with 0's) around an existing array | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#16-add-a-border-filled-with-0s-around-an-existing-array-) |
| **17** | [x] | Result of expressions with NaN and Inf | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#17-result-of-expressions-with-nan-and-inf-) |
| **18** | [x] | Create 5x5 matrix with values 1,2,3,4 below diagonal | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#18-create-a-5x5-matrix-with-values-1234-just-below-diagonal-) |
| **19** | [x] | Create 8x8 matrix with checkerboard pattern | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#19-create-an-8x8-matrix-and-fill-it-with-a-checkerboard-pattern-) |
| **20** | [x] | Shape (6,7,8) array: index (x,y,z) of 100th element | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#20-shape-678-array-index-xyz-of-100th-element-) |
| **21** | [ ] | Create checkerboard 8x8 matrix using `np.tile` | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#21-create-a-checkerboard-8x8-matrix-using-nptile-) |
| **22** | [ ] | Normalize a 5x5 random matrix | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#22-normalize-a-5x5-random-matrix-) |
| **23** | [ ] | Custom dtype describing RGBA color | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#23-create-custom-dtype-describing-rgba-color-4-unsigned-bytes-) |
| **24** | [ ] | Multiply 5x3 matrix by 3x2 matrix (`@`) | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#24-multiply-a-5x3-matrix-by-a-3x2-matrix-) |
| **25** | [ ] | Negate elements between 3 and 8 in place | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#25-given-1d-array-negate-all-elements-between-3-and-8-in-place-) |
| **26** | [ ] | Output of `sum(range(5), -1)` vs `np.sum` | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#26-output-of-sumrange5--1-vs-npsumrange5--1-) |
| **27** | [ ] | Legal expressions with integer vector Z | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#27-legal-expressions-with-integer-vector-z-) |
| **28** | [ ] | Floating point comparisons and expressions | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#28-result-of-floating-point-comparison-expressions-) |
| **29** | [ ] | Round away from zero for float array | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#29-how-to-round-away-from-zero-a-float-array-) |
| **30** | [ ] | Common values between two arrays | [02_indexing.ipynb](notebooks/02_indexing_slicing_and_reshaping.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#30-how-to-find-common-values-between-two-arrays-) |
| **31** | [ ] | How to ignore all numpy warnings | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#31-how-to-ignore-all-numpy-warnings-) |
| **32** | [ ] | Is `np.sqrt(-1) == np.emath.sqrt(-1)` true? | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#32-is-npsqrt-1--npemathsqrt-1-true-) |
| **33** | [ ] | Dates of yesterday, today, and tomorrow | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#33-get-dates-of-yesterday-today-and-tomorrow-) |
| **34** | [ ] | Dates corresponding to July 2016 | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#34-get-all-dates-corresponding-to-month-of-july-2016-) |
| **35** | [ ] | Compute `((A+B)*(-A/2))` in place | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#35-compute-ab-a2-in-place-without-copy-) |
| **36** | [ ] | Extract integer part of float array (4 methods) | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#36-extract-integer-part-of-float-array-using-4-methods-) |
| **37** | [ ] | 5x5 matrix with row values ranging 0 to 4 | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#37-create-a-5x5-matrix-with-row-values-ranging-from-0-to-4-) |
| **38** | [ ] | Build array from integer generator (`np.fromiter`) | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#38-build-array-from-a-generator-yielding-10-integers-) |
| **39** | [ ] | Vector of size 10 from 0 to 1 excluded | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#39-create-vector-of-size-10-from-0-to-1-both-excluded-) |
| **40** | [ ] | Random vector of size 10 sorted | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#40-create-a-random-vector-of-size-10-and-sort-it-) |
| **41** | [ ] | Sum small array faster than `np.sum` (`add.reduce`) | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#41-sum-a-small-array-faster-than-npsum-) |
| **42** | [ ] | Check if two random arrays A and B are equal | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#42-check-if-two-random-arrays-a-and-b-are-equal-) |
| **43** | [ ] | Make array immutable / read-only | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#43-make-an-array-immutable-read-only-) |
| **44** | [ ] | Convert Cartesian coordinates to polar coordinates | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#44-convert-10x2-cartesian-coordinates-to-polar-coordinates-) |
| **45** | [ ] | Replace maximum value in vector with 0 | [03_math.ipynb](notebooks/03_math_statistics_and_broadcasting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#45-create-random-vector-size-10-and-replace-max-value-with-0-) |
| **46** | [ ] | Structured array covering [0,1]x[0,1] | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#46-structured-array-with-x-y-coordinates-covering-01x01-) |
| **47** | [ ] | Cauchy matrix C construction | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#47-given-two-arrays-x-and-y-construct-cauchy-matrix-c-) |
| **48** | [ ] | Min/max limits for scalar dtypes (`iinfo`/`finfo`) | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#48-print-min-and-max-representable-values-for-scalar-dtypes-) |
| **49** | [ ] | Print all values without truncation | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#49-how-to-print-all-values-of-an-array-without-truncation-) |
| **50** | [ ] | Find closest value to given scalar | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#50-how-to-find-closest-value-to-given-scalar-in-a-vector-) |
| **51** | [ ] | Structured array: position (x,y) and color (r,g,b) | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#51-structured-array-representing-position-xy-and-color-rgb-) |
| **52** | [ ] | Point-by-point distances in (100,2) array | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#52-point-by-point-distances-in-shape-100-2-array-) |
| **53** | [ ] | Float32 to int32 in place via view | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#53-convert-float32-array-into-int32-in-place-) |
| **54** | [ ] | Read file using `genfromtxt` | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#54-how-to-read-file-with-genfromtxt-) |
| **55** | [ ] | Enumerate equivalent: `ndenumerate`, `ndindex` | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#55-what-is-equivalent-of-enumerate-for-numpy-arrays-) |
| **56** | [ ] | Generate a 2D Gaussian-like array | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#56-generate-a-generic-2d-gaussian-like-array-) |
| **57** | [ ] | Randomly place p elements in a 2D array | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#57-randomly-place-p-elements-in-a-2d-array-) |
| **58** | [ ] | Subtract mean of each row of a matrix | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#58-subtract-mean-of-each-row-of-a-matrix-) |
| **59** | [ ] | Sort array by the nth column (`argsort`) | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#59-how-to-sort-an-array-by-the-nth-column-) |
| **60** | [ ] | Check if 2D array has null columns | [04_random.ipynb](notebooks/04_random_sampling_and_sorting.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#60-how-to-tell-if-a-given-2d-array-has-null-columns-) |
| **61** | [ ] | Find nearest value from given target in array | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#61-find-nearest-value-from-given-target-in-an-array-) |
| **62** | [ ] | Sum (1,3) and (3,1) using `nditer` | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#62-sum-13-and-31-arrays-using-nditer-) |
| **63** | [ ] | Custom array subclass with a name attribute | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#63-create-an-array-class-that-has-a-name-attribute-) |
| **64** | [ ] | Add 1 to indexed elements (`np.add.at`) | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#64-add-1-to-elements-indexed-by-another-vector-handling-duplicates-) |
| **65** | [ ] | Accumulate vector elements by indices (`bincount`) | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#65-accumulate-vector-elements-based-on-index-list-) |
| **66** | [ ] | Compute unique colors in (w,h,3) image | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#66-compute-number-of-unique-colors-in-a-wh3-image-) |
| **67** | [ ] | Sum over last two axes of 4D array | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#67-sum-over-the-last-two-axes-of-a-4d-array-at-once-) |
| **68** | [ ] | Compute subset means via category array | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#68-compute-means-of-subsets-defined-by-category-array-) |
| **69** | [ ] | Diagonal of dot product efficiently ($O(N^2)$) | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#69-get-diagonal-of-dot-product-efficiently-) |
| **70** | [ ] | Interleave 3 zeros between elements | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#70-interleave-3-consecutive-zeros-between-vector-values-) |
| **71** | [ ] | Multiply (5,5,3) array by (5,5) array | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#71-multiply-553-array-by-55-array-) |
| **72** | [ ] | Swap two rows of an array in place | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#72-swap-two-rows-of-an-array-) |
| **73** | [ ] | Unique line segments from triangle mesh | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#73-unique-line-segments-from-set-of-triangles-) |
| **74** | [ ] | Invert `bincount` to produce source array | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#74-invert-bincount-to-produce-source-array-) |
| **75** | [ ] | Sliding window moving average | [05_dtypes.ipynb](notebooks/05_dtypes_and_structured_arrays.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#75-sliding-window-average-over-array-) |
| **76** | [ ] | Sliding 2D window via `sliding_window_view` | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#76-sliding-2d-window-matrix-using-stride-tricks-) |
| **77** | [ ] | In-place boolean negation / float sign inversion | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#77-in-place-boolean-negation--sign-inversion-) |
| **78** | [ ] | Distance from point to 2D line segments | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#78-distance-from-point-p-to-2d-lines-) |
| **79** | [ ] | Distance from points to line segments | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#79-distance-from-points-to-lines-) |
| **80** | [ ] | Centered subpart extraction with fill | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#80-centered-subpart-extraction-with-fill-) |
| **81** | [ ] | Rolling sub-arrays generation | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#81-rolling-sub-arrays-generation-) |
| **82** | [ ] | Compute matrix rank | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#82-compute-matrix-rank-) |
| **83** | [ ] | Most frequent value in an array (mode) | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#83-find-most-frequent-value-in-array-) |
| **84** | [ ] | Extract contiguous 3x3 blocks from 10x10 matrix | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#84-extract-contiguous-3x3-blocks-from-10x10-matrix-) |
| **85** | [ ] | Symmetric 2D array subclass | [06_linalg.ipynb](notebooks/06_linear_algebra_and_matrix_ops.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#85-symmetric-2d-array-subclass-) |
| **86** | [ ] | Sum of p matrix products at once (`np.einsum`) | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#86-sum-of-p-matrix-products-at-once-using-einsum-) |
| **87** | [ ] | Block-sum of 16x16 with 4x4 blocks | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#87-block-sum-of-16x16-array-with-4x4-blocks-) |
| **88** | [ ] | Conway's Game of Life vectorization | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#88-conways-game-of-life-vectorized-implementation-) |
| **89** | [ ] | Get n largest values of an array (`argpartition`) | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#89-get-n-largest-values-of-an-array-) |
| **90** | [ ] | Cartesian product of arbitrary vectors | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#90-cartesian-product-of-arbitrary-vectors-) |
| **91** | [ ] | Record array from regular array (`np.rec`) | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★☆☆` | [Check](solutions/reference_solutions.md#91-create-record-array-from-regular-array-) |
| **92** | [ ] | Large vector $Z^3$ computed with 3 methods | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#92-large-vector-z3-computed-with-3-methods-) |
| **93** | [ ] | Rows containing elements of another array | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#93-rows-containing-elements-of-another-array-) |
| **94** | [ ] | Extract rows with unequal values | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#94-extract-rows-with-unequal-values-from-10x3-matrix-) |
| **95** | [ ] | Integer vector to binary matrix (`unpackbits`) | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#95-convert-integer-vector-to-binary-matrix-) |
| **96** | [ ] | Extract unique rows from 2D array | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#96-extract-unique-rows-from-2d-array-) |
| **97** | [ ] | Einsum: inner, outer, sum, and mul | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★☆` | [Check](solutions/reference_solutions.md#97-npeinsum-equivalent-for-inner-outer-sum-and-mul-) |
| **98** | [ ] | Equidistant sampling of a 2D curve path | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#98-equidistant-sampling-of-a-2d-curve-path-) |
| **99** | [ ] | Select rows representing multinomial distribution | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#99-select-rows-from-multinomial-distribution-) |
| **100** | [ ] | Bootstrapped 95% confidence interval for mean | [07_einsum.ipynb](notebooks/07_advanced_vectorization_and_einsum.ipynb) | `★★★` | [Check](solutions/reference_solutions.md#100-bootstrapped-95-confidence-interval-for-mean-) |

</details>

---

## 🎖️ Acknowledgments & Credits

- **[Nicolas P. Rougier](https://github.com/rougier)** for creating the benchmark [100 numpy exercises](https://github.com/rougier/numpy-100).
- **[Keith Galli](https://www.youtube.com/@KeithGalli)** for the YouTube video challenge [Solving 100 Python NumPy Problems! (From easy to difficult)](https://www.youtube.com/watch?v=PM504XhEVCU).
- **The NumPy Development Team** for their foundational library.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

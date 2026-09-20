# NumPy 100 Mastery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, modern, beautifully structured GitHub repository (`numpy-100-mastery`) containing all 100 NumPy exercises from Nicolas P. Rougier and Keith Galli's video challenge, broken into 7 topic notebooks, a searchable cheatsheet, a verification test suite, and a badge-rich master README.

**Architecture:** 
- `notebooks/`: 7 modular Jupyter notebooks with rich explanations, intuition, primary solutions, alternatives, and gotchas for exercises 1–100.
- `cheatsheets/`: Single markdown fast-lookup cheatsheet containing all 100 solutions.
- `tests/`: Automated unit tests verifying modern NumPy 2.x solutions for key algorithmic exercises.
- `README.md`: High-impact landing page with master index, difficulty tags, video & creator attribution, progress tracker, and quickstart instructions.

**Tech Stack:** Python 3.10+, NumPy >= 2.0, Jupyter Notebook, Pytest, SVG Graphics.

---

### Task 1: Environment Configuration & Project Scaffolding

**Files:**
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `LICENSE`

- [ ] **Step 1: Create `.gitignore` for Python & Jupyter**
Include `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `*.pyc`, `.pytest_cache/`, and OS files.

- [ ] **Step 2: Create `requirements.txt`**
Specify `numpy>=2.0.0`, `jupyterlab>=4.0.0`, `notebook>=7.0.0`, `matplotlib>=3.8.0`, and `pytest>=8.0.0`.

- [ ] **Step 3: Create `LICENSE` (MIT License)**
Standard MIT License for open-source distribution.

- [ ] **Step 4: Verify files and commit**
Run: `git add .gitignore requirements.txt LICENSE; git commit -m "chore: setup repo configuration, dependencies, and license"`

---

### Task 2: Vector Graphic Banner (`assets/banner.svg`)

**Files:**
- Create: `assets/banner.svg`

- [ ] **Step 1: Design clean SVG banner**
Dimensions: 1200x320. Modern dark gradient background (`#0d1117` to `#161b22`), NumPy blue accent glow (`#4D77CF`, `#013243`), modern typography, badge pills ("100 Exercises", "NumPy 2.x Ready", "Video Walkthrough Included").

- [ ] **Step 2: Validate SVG syntax**
Verify the SVG file is well-formed XML and renders cleanly without missing closing tags.

- [ ] **Step 3: Commit**
Run: `git add assets/banner.svg; git commit -m "feat(assets): add modern NumPy 100 mastery SVG banner"`

---

### Task 3: Fast Reference Cheatsheet (`cheatsheets/all_100_solutions.md`)

**Files:**
- Create: `cheatsheets/all_100_solutions.md`

- [ ] **Step 1: Write all 100 problem statements and concise solutions**
Organized into the 7 defined categories with difficulty badges (`★☆☆`, `★★☆`, `★★★`). Each exercise has:
- Exercise number and problem statement
- 1-4 lines of idiomatic, modern NumPy code
- Markdown anchor links for fast browser navigation

- [ ] **Step 2: Verify all 100 exercises are present**
Ensure exercises 1 through 100 are strictly sequential with no omissions or numbering gaps.

- [ ] **Step 3: Commit**
Run: `git add cheatsheets/all_100_solutions.md; git commit -m "feat: add complete 100 numpy exercises fast-lookup cheatsheet"`

---

### Task 4: Topic Notebooks 1 & 2 (Exercises 1–30)

**Files:**
- Create: `notebooks/01_array_creation_and_basics.ipynb` (Ex 1–15)
- Create: `notebooks/02_indexing_slicing_and_reshaping.ipynb` (Ex 16–30)

- [ ] **Step 1: Build Notebook 01 (`01_array_creation_and_basics.ipynb`)**
Exercises 1–15 covering import, version, configuration, null vector, memory footprint (`nbytes`), CLI docs, reverse slice (`[::-1]`), 3x3 matrices, non-zero indices (`np.nonzero`), identity matrices (`np.eye`), 3D random arrays, min/max, mean, and border creation.
Each exercise includes Markdown (Intuition, Difficulty, Gotcha) and executable Code cells.

- [ ] **Step 2: Build Notebook 02 (`02_indexing_slicing_and_reshaping.ipynb`)**
Exercises 16–30 covering `np.pad`, NaN/Inf arithmetic, `np.diag`, checkerboard patterns (`np.tile` vs strided slice), `np.unravel_index`, matrix normalization, custom RGBA dtypes, matrix multiplication (`@`), conditional in-place negation, `sum` vs `np.sum`, float expressions, rounding away from zero, and `np.intersect1d`.

- [ ] **Step 3: Validate Notebook JSON structure**
Run Python validation script to parse `.ipynb` JSON and confirm cell structures and metadata are valid.

- [ ] **Step 4: Commit**
Run: `git add notebooks/01_array_creation_and_basics.ipynb notebooks/02_indexing_slicing_and_reshaping.ipynb; git commit -m "feat(notebooks): add notebooks 01 and 02 covering exercises 1 to 30"`

---

### Task 5: Topic Notebooks 3 & 4 (Exercises 31–60)

**Files:**
- Create: `notebooks/03_math_statistics_and_broadcasting.ipynb` (Ex 31–45)
- Create: `notebooks/04_random_sampling_and_sorting.ipynb` (Ex 46–60)

- [ ] **Step 1: Build Notebook 03 (`03_math_statistics_and_broadcasting.ipynb`)**
Exercises 31–45 covering warning filters, complex square roots (`np.emath`), `datetime64` manipulation, in-place arithmetic without temporaries, integer extraction methods, `fromiter` generators, `linspace`, `np.sort`, fast reductions (`np.add.reduce`), array equality comparisons (`np.allclose`), read-only views, polar coordinate conversions, and max value replacement.

- [ ] **Step 2: Build Notebook 04 (`04_random_sampling_and_sorting.ipynb`)**
Exercises 46–60 covering 2D grid coordinates, Cauchy matrices, scalar type limits (`iinfo`/`finfo`), print options, closest value search, position+color records, point-to-point distances, in-place dtype conversions, `genfromtxt`, `ndenumerate`/`ndindex`, 2D Gaussian arrays, random element placement (`np.put`), row-wise centering, column sorting (`argsort`), and null column detection.

- [ ] **Step 3: Validate Notebook JSON structure**
Run validation script to ensure valid notebook formatting.

- [ ] **Step 4: Commit**
Run: `git add notebooks/03_math_statistics_and_broadcasting.ipynb notebooks/04_random_sampling_and_sorting.ipynb; git commit -m "feat(notebooks): add notebooks 03 and 04 covering exercises 31 to 60"`

---

### Task 6: Topic Notebooks 5, 6 & 7 (Exercises 61–100)

**Files:**
- Create: `notebooks/05_dtypes_and_structured_arrays.ipynb` (Ex 61–75)
- Create: `notebooks/06_linear_algebra_and_matrix_ops.ipynb` (Ex 76–85)
- Create: `notebooks/07_advanced_vectorization_and_einsum.ipynb` (Ex 86–100)

- [ ] **Step 1: Build Notebook 05 (`05_dtypes_and_structured_arrays.ipynb`)**
Exercises 61–75 covering nearest value search, `nditer` broadcasting, array subclassing with metadata, repeated index accumulation (`np.add.at`, `bincount`), unique colors in images, multi-axis reductions, subset means, diagonal dot products, interleaved zeros, 3D x 2D broadcasting, row swapping, triangle edge extraction, `bincount` inversion, and sliding window averages.

- [ ] **Step 2: Build Notebook 06 (`06_linear_algebra_and_matrix_ops.ipynb`)**
Exercises 76–85 covering sliding window views, in-place sign manipulation, 2D line distance calculations, centered sub-array extraction, rolling sub-arrays, matrix rank (`np.linalg.matrix_rank`), mode computation, contiguous block extraction, and symmetric array subclassing.

- [ ] **Step 3: Build Notebook 07 (`07_advanced_vectorization_and_einsum.ipynb`)**
Exercises 86–100 covering batch matrix products with `np.einsum`, 2D block-sums, Conway's Game of Life vectorization, `np.argpartition` for top-N values, Cartesian products, record arrays, power operations benchmarking, row subset matching, binary representation of integers, unique rows, einsum operations (inner, outer, mul, sum), equidistant curve sampling, multinomial row extraction, and bootstrap confidence intervals.

- [ ] **Step 4: Validate Notebook JSON structure**
Run validation script to verify all 7 notebooks pass parsing without error.

- [ ] **Step 5: Commit**
Run: `git add notebooks/05_dtypes_and_structured_arrays.ipynb notebooks/06_linear_algebra_and_matrix_ops.ipynb notebooks/07_advanced_vectorization_and_einsum.ipynb; git commit -m "feat(notebooks): add notebooks 05, 06, and 07 covering exercises 61 to 100"`

---

### Task 7: Verification Test Suite (`tests/test_exercises.py`)

**Files:**
- Create: `tests/test_exercises.py`

- [ ] **Step 1: Write automated tests for representative exercises across all 7 sections**
Cover:
- Array creation and reversing
- Memory size calculations
- Border padding and checkerboard patterns
- Cauchy matrix construction
- In-place operations without copies
- Sliding window view and rolling averages
- Vectorized Game of Life step
- Einsum batch matrix multiplication and equivalences
- Bootstrap mean estimation

- [ ] **Step 2: Run pytest to verify all tests pass**
Run: `python -m pytest tests/test_exercises.py -v` (or standard `unittest` via python runner)
Expected: All tests PASS.

- [ ] **Step 3: Commit**
Run: `git add tests/test_exercises.py; git commit -m "test: add automated verification suite for numpy exercises"`

---

### Task 8: Master README & Repository Landing Hub (`README.md`)

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write the master README**
Include:
- Embedded SVG banner (`assets/banner.svg`)
- Shields.io badges (Python, NumPy 2.x, Jupyter, License MIT, Challenges 100/100)
- Overview & Highlights (What makes this repo distinct)
- Quickstart guide (clone, virtual environment setup, launching JupyterLab)
- Interactive Master Table of Contents with:
  - Exercise #
  - Title / Prompt
  - Topic Notebook Link
  - Difficulty (`★☆☆`, `★★☆`, `★★★`)
  - Status checkbox
- Video & Original Author Acknowledgments (Keith Galli YouTube video embed link, Nicolas P. Rougier original GitHub link)
- Contributing & License info

- [ ] **Step 2: Verify links and anchors**
Ensure all relative markdown links to `notebooks/*.ipynb` and `cheatsheets/all_100_solutions.md` are valid.

- [ ] **Step 3: Commit**
Run: `git add README.md; git commit -m "docs: add comprehensive interactive master README with 100 exercise tracker"`

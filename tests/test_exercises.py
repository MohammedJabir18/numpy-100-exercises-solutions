"""
Automated Verification Test Suite for NumPy 100 Mastery Exercises.
Tests key computational logic, modern NumPy 2.x idioms, and algorithmic patterns.
Can be executed via `python -m unittest tests/test_exercises.py` or `pytest tests/`.
"""

import unittest
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


class TestNumpy100Mastery(unittest.TestCase):

    def test_ex04_memory_size(self):
        arr = np.zeros((10, 10), dtype=np.float64)
        expected_bytes = 10 * 10 * 8
        self.assertEqual(arr.nbytes, expected_bytes)
        self.assertEqual(arr.size * arr.itemsize, expected_bytes)

    def test_ex08_vector_reverse(self):
        Z = np.arange(10)
        rev = Z[::-1]
        flipped = np.flip(Z)
        np.testing.assert_array_equal(rev, np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
        np.testing.assert_array_equal(rev, flipped)

    def test_ex15_border_ones(self):
        Z = np.ones((5, 5), dtype=int)
        Z[1:-1, 1:-1] = 0
        self.assertEqual(Z.sum(), (5 * 5) - (3 * 3))
        self.assertTrue(np.all(Z[1:-1, 1:-1] == 0))
        self.assertTrue(np.all(Z[0, :] == 1))
        self.assertTrue(np.all(Z[-1, :] == 1))

    def test_ex16_pad_border(self):
        Z = np.ones((3, 3), dtype=int)
        padded = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
        self.assertEqual(padded.shape, (5, 5))
        self.assertTrue(np.all(padded[1:-1, 1:-1] == 1))
        self.assertEqual(padded[0, 0], 0)

    def test_ex18_subdiagonal(self):
        Z = np.diag(1 + np.arange(4), k=-1)
        self.assertEqual(Z.shape, (5, 5))
        np.testing.assert_array_equal(np.diagonal(Z, offset=-1), np.array([1, 2, 3, 4]))
        self.assertTrue(np.all(np.diagonal(Z, offset=0) == 0))

    def test_ex19_checkerboard(self):
        Z = np.zeros((8, 8), dtype=int)
        Z[1::2, ::2] = 1
        Z[::2, 1::2] = 1
        self.assertEqual(Z.sum(), 32)
        self.assertEqual(Z[0, 0], 0)
        self.assertEqual(Z[0, 1], 1)
        self.assertEqual(Z[1, 0], 1)
        self.assertEqual(Z[1, 1], 0)

    def test_ex20_unravel_index(self):
        coords = np.unravel_index(99, (6, 7, 8))
        self.assertEqual(coords, (1, 5, 3))

    def test_ex24_matrix_multiplication(self):
        A = np.ones((5, 3))
        B = np.ones((3, 2)) * 2
        C = A @ B
        self.assertEqual(C.shape, (5, 2))
        self.assertTrue(np.all(C == 6.0))

    def test_ex29_round_away_from_zero(self):
        Z = np.array([-3.2, -0.5, 0.0, 0.5, 3.2])
        rounded = np.copysign(np.ceil(np.abs(Z)), Z)
        np.testing.assert_array_equal(rounded, np.array([-4.0, -1.0, 0.0, 1.0, 4.0]))

    def test_ex35_inplace_arithmetic(self):
        A = np.ones(3) * 4
        B = np.ones(3) * 2
        # Target: ((A+B)*(-A/2)) = (4+2)*(-2) = -12
        np.add(A, B, out=B)
        np.divide(A, 2, out=A)
        np.negative(A, out=A)
        np.multiply(A, B, out=A)
        self.assertTrue(np.all(A == -12.0))

    def test_ex47_cauchy_matrix(self):
        X = np.arange(4)
        Y = X + 0.5
        C = 1.0 / np.subtract.outer(X, Y)
        self.assertEqual(C.shape, (4, 4))
        self.assertTrue(np.isclose(C[0, 0], -2.0))

    def test_ex64_np_add_at(self):
        Z = np.zeros(6, dtype=int)
        I = np.array([1, 2, 2, 2, 4, 4])
        np.add.at(Z, I, 1)
        np.testing.assert_array_equal(Z, np.array([0, 1, 3, 0, 2, 0]))

    def test_ex69_diagonal_dot_product(self):
        rng = np.random.default_rng(42)
        A = rng.random((20, 20))
        B = rng.random((20, 20))
        slow_diag = np.diag(A @ B)
        fast_diag = np.sum(A * B.T, axis=1)
        self.assertTrue(np.allclose(slow_diag, fast_diag))

    def test_ex74_invert_bincount(self):
        C = np.array([0, 2, 3, 1, 0, 4])
        A = np.repeat(np.arange(len(C)), C)
        np.testing.assert_array_equal(np.bincount(A, minlength=len(C)), C)

    def test_ex75_moving_average(self):
        def moving_average(a, n=3):
            ret = np.cumsum(a, dtype=float)
            ret[n:] = ret[n:] - ret[:-n]
            return ret[n - 1:] / n

        Z = np.array([1, 2, 3, 4, 5, 6], dtype=float)
        ma = moving_average(Z, n=3)
        self.assertTrue(np.allclose(ma, np.array([2.0, 3.0, 4.0, 5.0])))

    def test_ex76_sliding_window_view(self):
        Z = np.arange(6)
        windows = sliding_window_view(Z, window_shape=3)
        self.assertEqual(windows.shape, (4, 3))
        np.testing.assert_array_equal(windows[0], [0, 1, 2])
        np.testing.assert_array_equal(windows[-1], [3, 4, 5])

    def test_ex85_symmetric_array(self):
        class SymArray(np.ndarray):
            def __setitem__(self, index, value):
                i, j = index
                super().__setitem__((i, j), value)
                super().__setitem__((j, i), value)

        Z = np.zeros((3, 3)).view(SymArray)
        Z[0, 2] = 42
        self.assertEqual(Z[0, 2], 42)
        self.assertEqual(Z[2, 0], 42)

    def test_ex86_einsum_batch_matrix_products(self):
        p, n = 4, 3
        M = np.ones((p, n, n)) * 2
        V = np.ones((p, n, 1)) * 3
        einsum_res = np.einsum('ijk,ikl->jl', M, V)
        self.assertEqual(einsum_res.shape, (n, 1))
        self.assertTrue(np.all(einsum_res == 72.0))

    def test_ex88_conway_game_of_life(self):
        def iterate_life(Z):
            N = (Z[0:-2, 0:-2] + Z[0:-2, 1:-1] + Z[0:-2, 2:] +
                 Z[1:-1, 0:-2]                 + Z[1:-1, 2:] +
                 Z[2:  , 0:-2] + Z[2:  , 1:-1] + Z[2:  , 2:])
            birth = (N == 3) & (Z[1:-1, 1:-1] == 0)
            survive = ((N == 2) | (N == 3)) & (Z[1:-1, 1:-1] == 1)
            Z[...] = 0
            Z[1:-1, 1:-1][birth | survive] = 1
            return Z

        grid = np.zeros((5, 5), dtype=int)
        grid[2, 1:4] = 1

        # Step 1: turns into vertical blinker
        grid = iterate_life(grid)
        self.assertTrue(np.all(grid[:, 2] == np.array([0, 1, 1, 1, 0])))
        self.assertEqual(grid.sum(), 3)

        # Step 2: returns to horizontal blinker
        grid = iterate_life(grid)
        self.assertTrue(np.all(grid[2, :] == np.array([0, 1, 1, 1, 0])))
        self.assertEqual(grid.sum(), 3)

    def test_ex97_einsum_equivalences(self):
        A = np.array([1, 2, 3])
        B = np.array([4, 5, 6])
        self.assertEqual(np.einsum('i,i->', A, B), np.inner(A, B))
        np.testing.assert_array_equal(np.einsum('i,j->ij', A, B), np.outer(A, B))
        self.assertEqual(np.einsum('i->', A), np.sum(A))
        np.testing.assert_array_equal(np.einsum('i,i->i', A, B), A * B)

    def test_ex100_bootstrap_confidence_interval(self):
        rng = np.random.default_rng(42)
        true_mean = 5.0
        X = rng.normal(loc=true_mean, scale=1.0, size=200)

        n_boot = 1000
        boot_indices = rng.integers(0, len(X), (n_boot, len(X)))
        boot_means = X[boot_indices].mean(axis=1)
        ci_lower, ci_upper = np.percentile(boot_means, [2.5, 97.5])

        self.assertTrue(ci_lower < true_mean < ci_upper)


if __name__ == '__main__':
    unittest.main()

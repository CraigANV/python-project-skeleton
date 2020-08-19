#!/usr/bin/env python3

import numpy as np


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


def test_numpy():
    print("\nVector Multiplication: dot(v_a, v_b)\n")

    v_a = np.arange(1, 9)
    v_b = np.arange(8, 0, -1)

    # If both arrays are 1d dot() does vector inner product
    v_ab = np.dot(v_a, v_b)
    print(v_ab, v_ab.shape)

    assert (np.dot(v_a, v_b) == v_a @ v_b)
    assert (np.dot(v_a, v_b) == np.vdot(v_a, v_b))
    assert (np.dot(v_a, v_b) == np.inner(v_a, v_b))
    assert (np.dot(v_a, v_b) == v_a.dot(v_b))
    assert (np.dot(v_a, v_b) == np.matmul(v_a, v_b))


def main():
    test_numpy()


if __name__ == "__main__":
    main()

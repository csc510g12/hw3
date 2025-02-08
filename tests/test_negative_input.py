"""This module contains tests for handling negative inputs."""
import pytest

from hw3.hw2_debugging import merge_sort


@pytest.mark.parametrize(
    "input_arr, expected_output",
    [([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1])],
)
def test_mergesort(input_arr, expected_output):
    """Tests how the system handles negative inputs."""
    assert merge_sort(input_arr) == expected_output


if __name__ == "__main__":
    pytest.main()

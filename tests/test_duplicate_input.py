"""This module contains tests for handling duplicate inputs."""
import pytest

from hw3.hw2_debugging import merge_sort


@pytest.mark.parametrize(
    "input_arr, expected_output", [([1, 3, 2, 3, 2, 1], [1, 1, 2, 2, 3, 3])]
)
def test_mergesort(input_arr, expected_output):
    """Tests how the system handles duplicate inputs."""
    assert merge_sort(input_arr) == expected_output


if __name__ == "__main__":
    pytest.main()

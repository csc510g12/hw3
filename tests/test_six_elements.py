import pytest

# import hw3.rand as rand
from hw3.hw2_debugging import merge_sort


@pytest.mark.parametrize(
    "input_arr, expected_output",
    [
        ([3, 13, 3, 5, 9, 11], [3, 3, 5, 9, 11, 13]),
        ([9, 12, 3, 12, 8, 1], [1, 3, 8, 9, 12, 12]),
        ([16, 14, 5, 5, 19, 3], [3, 5, 5, 14, 16, 19]),
    ],
)
def test_merge_sort(input_arr, expected_output):
    assert merge_sort(input_arr) == expected_output


if __name__ == "__main__":
    pytest.main()

import pytest

# import hw3.rand as rand
from hw3.hw2_debugging import merge_sort


@pytest.mark.parametrize(
    "input_arr, expected_output",
    [
        ([1], [1]),  # Single-element list
    ],
)
def test_merge_sort(input_arr, expected_output):
    assert merge_sort(input_arr) == expected_output


if __name__ == "__main__":
    pytest.main()

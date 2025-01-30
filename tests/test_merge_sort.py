import pytest
import hw3.rand as rand
from hw3.hw2_debugging import mergeSort  

@pytest.mark.parametrize("input_arr, expected_output", [
    ([], []),  # Empty list
    ([1], [1]),  # Single-element list
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse order
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])),  # Random order
])
def test_mergeSort(input_arr, expected_output):
    assert mergeSort(input_arr) == expected_output

def test_random_array():
    """Test mergeSort with a randomly generated array"""
    arr = rand.random_array([None] * 20)
    sorted_arr = mergeSort(arr)
    assert sorted_arr == sorted(arr), "mergeSort failed on a random array"

if __name__ == "__main__":
    pytest.main()

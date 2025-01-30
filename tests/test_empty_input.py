import pytest
import hw3.rand as rand
from hw3.hw2_debugging import mergeSort  

@pytest.mark.parametrize("input_arr, expected_output", [
    ([], []),  # Empty list
])
def test_mergeSort(input_arr, expected_output):
    assert mergeSort(input_arr) == expected_output

if __name__ == "__main__":
    pytest.main()

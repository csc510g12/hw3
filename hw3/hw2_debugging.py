from hw3 import rand


def merge_sort(arr):
    # print(f"Array: {arr}")
    if (len(arr) == 1) or len(arr) == 0:
        return arr

    half = len(arr) // 2

    # print(f"{arr[:half], arr[half:]}")

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    left_index = 0
    right_index = 0
    # merge_arr = [None] * (len(left_arr) + len(right_arr))
    merge_arr = []
    # print(f"merge_arr (before): {merge_arr}")
    while left_index < len(left_arr) and right_index < len(right_arr):
        # print(f"{left_arr}, {right_arr}")
        # print(f"Left index: {left_index}, Right index: {right_index}")
        # print(f"Right Array: {right_arr[right_index]}")
        # print(f"Left Array: {left_arr[left_index]}")
        # if left_arr[left_index] < right_arr[right_index]:
        #     right_index += 1
        #     merge_arr[left_index + right_index] = left_arr[left_index]
        # else:
        #     left_index += 1
        #     merge_arr[left_index + right_index] = right_arr[right_index]
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(right_arr[right_index:])
    merge_arr.extend(left_arr[left_index:])

    # print(f"Merge Array: {merge_arr}")
    return merge_arr


test_arr = rand.random_array([None] * 6)
# arr = [3, 9, 16, 2, 8, 3]
print(f"Starting Array: {test_arr}")
arr_out = merge_sort(test_arr)

print(arr_out)

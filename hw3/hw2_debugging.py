import hw3.rand as rand

def mergeSort(arr):
    # print(f"Array: {arr}")
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    # print(f"{arr[:half], arr[half:]}")

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    # mergeArr = [None] * (len(leftArr) + len(rightArr))
    mergeArr = []
    # print(f"mergeArr (before): {mergeArr}")
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        # print(f"{leftArr}, {rightArr}")
        # print(f"Left index: {leftIndex}, Right index: {rightIndex}")
        # print(f"Right Array: {rightArr[rightIndex]}")
        # print(f"Left Array: {leftArr[leftIndex]}")
        # if leftArr[leftIndex] < rightArr[rightIndex]:
        #     rightIndex += 1
        #     mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        # else:
        #     leftIndex += 1
        #     mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1
    
    mergeArr.extend(rightArr[rightIndex:])
    mergeArr.extend(leftArr[leftIndex:])

    # print(f"Merge Array: {mergeArr}")
    return mergeArr

arr = rand.random_array([None] * 6)
# arr = [3, 9, 16, 2, 8, 3]
print(f"Starting Array: {arr}")
arr_out = mergeSort(arr)

print(arr_out)



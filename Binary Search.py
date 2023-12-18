def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
sorted_array = [11, 12, 22, 25, 34, 64, 90]
target_value = 25
result = binary_search(sorted_array, target_value)
print("Index of", target_value, ":", result)

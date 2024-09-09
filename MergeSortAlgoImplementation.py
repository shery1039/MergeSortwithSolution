# Define the merge_sort function
def merge_sort(arr):
    # Base case: if the array has 1 or fewer elements, return it (since it's already sorted)
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2

    # Recursively sort the left and right halves of the array
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted left and right halves
    return merge(left, right)

# Define the merge function
def merge(left, right):
    # Initialize an empty result array
    result = []
    i, j = 0, 0

    # Merge smaller elements from left and right arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left and right arrays
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Test the merge_sort function
a = [5, 7, 3, -5, -8, 0, -34]
merge_sort(a)  # This call is unnecessary, as it doesn't store the result
Result = merge_sort(a)
print(Result)  # [-34, -8, -5, 0, 3, 5, 7]
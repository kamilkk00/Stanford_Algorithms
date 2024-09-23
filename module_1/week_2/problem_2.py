# Read the array from the file
with open('integer_array.txt', 'r') as f:
    arr = list(map(int, f.readlines()))
 
# Initialize the necessary variables
left, right = 0, len(arr) - 1
temp_arr = [0] * len(arr)
inv_count = 0
stack = [(left, right)]

# Process each subarray in the stack
while stack:
    left, right = stack.pop()
    if left >= right:
        continue

    # Find the middle point of the current subarray
    mid = (left + right) // 2
    stack.append((left, mid))
    stack.append((mid + 1, right))
    
    # Initialize pointers for merging and counting inversions
    i, j, k, sub_inv_count = left, mid + 1, left, 0
    
    # Merge the two subarrays while counting inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            sub_inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy any remaining elements from the left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from the right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged subarray back into the original array
    arr[left:right + 1] = temp_arr[left:right + 1]
    
    # Add the count of inversions from this merge to the total count
    inv_count += sub_inv_count

# Print the total number of inversions
print(inv_count)

# Output: 2455824972
import random 

# Reading array
with open("array_quicksort.txt", "r") as file: 
    array = list(map(int, file.readlines()))

def main():
    # Making global count of comparisons 
    global comparisons
    comparisons = 0

    n = len(array)

    # Sort of array
    quick_sort(array, 0, n - 1)

    print("All comparions:", comparisons)


def quick_sort(a, l, r):
    global comparisons

    # If the subarray has less than 2 elements do nothing 
    if l >= r:
        return
    else:
        # Pivot number 
        pivot_index = pivot(a, l, r)

        # Partition the array around pivot 
        pivot_index = partition(a, l, r, pivot_index)

        # Updating global value 
        comparisons += r - l

        # Recursively sort elements around pivot 
        quick_sort(a, l, pivot_index - 1)
        quick_sort(a, pivot_index + 1, r)


def partition(a, l, r, pivot_index):
    # Seting new pivot position 
    new = a[pivot_index]
    a[pivot_index] = a[l]
    a[l] = new
    pivot = a[l]

    # Initialize element greater than pivot 
    i = l  + 1 

    # Checking undertable and reorganization 
    for j in range(l + 1, r + 1):
        if a[j] < pivot:
            # Sorting values 
            x = a[i]
            a[i] = a[j]
            a[j] = x
            i = i + 1
    
    # Changing pivot value 
    y = a[l]
    a[l] = a[i - 1]
    a[i - 1] = y

    # Returning pivot
    return i - 1

def pivot(a, l, r):
    # Pivot as first element 
    #return l 

    # Pivot as last element
    #return r 

    # Pivot as a median of three elements 
    first= l
    middle = l + (r - l) // 2
    last = r

    first_value = a[first] 
    last_value = a[last] 
    middle = l + (r - l) // 2 
    middle_value = a[middle]
    if (first_value <= middle_value <= last_value) or (last_value <= middle_value <= first_value):
        return middle
    elif (middle_value <= first_value <= last_value) or (last_value <= first_value <= middle_value):
        return first
    else: 
        return last
    
    



if __name__ == "__main__":
    main()

# first (l)  Output: 162085
# last (r) Output: 164123
# media_of_three Output: 138382
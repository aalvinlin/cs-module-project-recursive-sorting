# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(array_left, array_right):

    total_entries = len(array_left) + len(array_right)
    merged_array = [0] * total_entries

    # initialize pointers for start of each array
    next_smallest_left_index = 0
    next_smallest_right_index = 0

    print("    merging...", array_left, array_right, total_entries)

    for i in range(total_entries):

        # if the array_left has no more elements to add, append the rest of array_right and return
        if next_smallest_left_index >= len(array_left):
            return merged_array.extend(array_right[next_smallest_right_index:])

        # if the array_right has no more elements to add, append the rest of array_left and return
        elif next_smallest_right_index >= len(array_right):
            return merged_array.extend(array_left[next_smallest_left_index:])

        # add an entry from the left array if the left value is smaller
        elif array_left[next_smallest_left_index] < array_right[next_smallest_right_index]:
            merged_array[i] = array_left[next_smallest_left_index]
            next_smallest_left_index += 1
        
        # add an entry from the right array if the right value is smaller
        else:
            merged_array[i] = array_right[next_smallest_right_index]
            next_smallest_right_index += 1

    print("    merged array is", merged_array)

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    print("input is", arr, "with length", len(arr))

    # base case: an array of a single element is sorted
    if len(arr) <= 1:
        return arr
    
    # divide array into left and right halves
    start_of_right_half = len(arr) // 2

    left_half = arr[0:start_of_right_half]
    right_half = arr[start_of_right_half:]

    print("  left and right are", left_half, right_half)

    return merge(merge_sort(left_half), merge_sort(right_half))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

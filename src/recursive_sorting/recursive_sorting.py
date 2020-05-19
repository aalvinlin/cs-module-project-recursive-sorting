# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(array_left, array_right):

    total_entries = len(array_left) + len(array_right)
    merged_array = [0] * total_entries

    # initialize pointers for start of each array
    next_smallest_left_index = 0
    next_smallest_right_index = 0

    next_smallest_value_in_left_array = array_left[next_smallest_left_index]
    next_smallest_value_in_right_array = array_right[next_smallest_right_index]

    for i in range(total_entries):

        # add an entry from the left array if...
        #    there is a value in the left array but no values remaining in the right array
        #    both values exist and the left value is smaller
        if (next_smallest_value_in_left_array and not next_smallest_value_in_right_array) or (next_smallest_value_in_left_array < next_smallest_value_in_right_array):
            merged_array[i] = next_smallest_value_in_left_array
            next_smallest_left_index += 1
        
        # add an entry from the right array if...
        #    there is a value in the right array but no values remaining in the left array
        #    both values exist and the right value is smaller
        elif (next_smallest_value_in_right_array and not next_smallest_value_in_left_array) or (next_smallest_value_in_right_array <= next_smallest_value_in_left_array):
            merged_array[i] = next_smallest_value_in_right_array
            next_smallest_right_index += 1

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # base case: an array of a single element is sorted
    if len(arr) == 1:
        return arr
    
    # divide array into left and right halves
    start_of_right_half = len(arr) // 2

    left_half = arr[0:start_of_right_half - 1]
    right_half = arr[start_of_right_half:]

    return merge(merge_sort(left_half, right_half))


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

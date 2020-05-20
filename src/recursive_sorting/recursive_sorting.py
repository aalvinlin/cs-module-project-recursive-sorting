# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(array_left, array_right):

    total_entries = len(array_left) + len(array_right)
    merged_array = [0] * total_entries

    # initialize pointers for start of each array
    next_smallest_left_index = 0
    next_smallest_right_index = 0

    for i in range(total_entries):

        # if array_left has no more elements to add, append the rest of array_right
        if next_smallest_left_index == len(array_left):

            while next_smallest_right_index < len(array_right):
                merged_array[i] = array_right[next_smallest_right_index]
                i += 1
                next_smallest_right_index += 1

        # if array_right has no more elements to add, append the rest of array_left
        elif next_smallest_right_index == len(array_right):

            while next_smallest_left_index < len(array_left):
                merged_array[i] = array_left[next_smallest_left_index]
                i += 1
                next_smallest_left_index += 1

        # add an entry from the left array if the left value is smaller
        elif array_left[next_smallest_left_index] < array_right[next_smallest_right_index]:
            merged_array[i] = array_left[next_smallest_left_index]
            next_smallest_left_index += 1
        
        # add an entry from the right array if the right value is smaller
        else:
            merged_array[i] = array_right[next_smallest_right_index]
            next_smallest_right_index += 1

    return merged_array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # base case: an array of a single element is sorted
    if len(arr) <= 1:
        return arr
    
    # divide array into left and right halves
    start_of_right_half = len(arr) // 2

    left_half = arr[0:start_of_right_half]
    right_half = arr[start_of_right_half:]

    return merge(merge_sort(left_half), merge_sort(right_half))

# ===================== in-place merge sort algorithm ===================== 

# shift every element from start_index to end_index, inclusive, to the right by one.
# The element at index (end_index + 1) will be overwritten.
# There will be two copies of the element at start_index when finished: at start_index and at (start_index + 1).
def shift_section_one_space_right(arr, start_index, end_index):
    
    for i in range (end_index, start_index - 1, -1):
        arr[i + 1] = arr[i]

# shift every element from start_index to end_index, inclusive, to the left by n spaces.
# The element at index (start_index - 1) will be overwritten.
# There will be two copies of the element at end_index when finished: at end_index and at (end_index + 1).
# def shift_section_one_space_left(arr, start_index, end_index):
    
#     for i in range (start_index, end_index + 1):
#         arr[i - 1] = arr[i]

def merge_in_place(arr, start, mid, end):
    
    # initialize pointers for start of each array
    next_smallest_left_index = start
    next_smallest_right_index = mid

    # determine the total number of elements in this section
    total_elements = (end - start) + 1

    for i in range(total_elements):

        ## if the left array has no more elements to add, there is nothing left to do
        ## (the remaining elements on the right are already in the correct spots)


        # if the next smallest right index is the end of the array, there is nothing left to do
        # (all other elements would have been placed already). Any unprocessed elements would automatically be in the right place.
        if next_smallest_right_index == end:
            return

        # # if the right array has no more elements to add, add the rest of the array on the left
        # # this will require shifting elements over to the left to accomodate the incoming values
        # elif next_smallest_right_index == end:

        #     # save the value on the right (it will be overriden in a moment)
        #     value_to_move = arr[next_smallest_right_index]

        #     # shift the array one spot over to make room for the incoming value (value_to_move)
        #     # assumption is that the array only needs to be shifted over one
        #     shift_section_one_space_left(arr, mid, end_index - 1)

        # add an entry from the left array if the left value is smaller
        elif arr[next_smallest_left_index] < arr[next_smallest_right_index]:

            # if the value on the left is smaller, then it is in the right place already

            # update the pointer for the next smallest value on the left
            next_smallest_left_index += 1
        
        # add an entry from the right array if the right value is smaller
        else:

            # if the value on the right is smaller, then it needs to go in the spot currently occupied by the next smallest value on the left

            # save the value on the right (it will be overriden in a moment)
            value_to_move = arr[next_smallest_right_index]

            # shift the array one spot over to make room for the incoming value (value_to_move)
            shift_section_one_space_right(arr, next_smallest_left_index, next_smallest_right_index - 1)
           
            # move the pointer to the next smaller value on the right
            next_smallest_right_index += 1

            # place value_to_move in the spot currently occupied by the next smaller value on the left
            arr[next_smallest_left_index] = value_to_move

            # move the pointer to the next smaller value on the left
            next_smallest_left_index += 1

    return arr


def merge_sort_in_place(arr, left_half_start_index, right_half_end_index):
    
    # base case: an array of a single element is sorted
    if len(arr) <= 1:
        return arr

    # divide array into left and right halves
    start_of_right_half = len(arr) // 2 + left_half_start_index

    return merge_in_place(merge_sort_in_place(left_half_start_index, start_of_right_half, right_half_end_index))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

# Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        #: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr
arr = [2,7,9,1,5,0,3,8,4,6]
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # boolean of whether swap happened for while loop existence
    swapped = True
    # while variable True
    while swapped:
        swapped = False
        # loop over array  
        for i in range(0, len(arr)-1):
            # swap current index with next index if current is greater than next
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True



    return arr
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if len(arr) == 0:
        return arr
    if maximum == -1:
        arr_max = max(arr)
    # TODO make a count array that counts the instances of each value in passed array
    count_arr = [0 for i in range(arr_max + 1)]
    # TODO loop over passed array and make counts at the correct indexes in count array
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return 'Error, negative numbers not allowed in Count Sort'
        else:
            count_arr[arr[i]] += 1
    # TODO loop over count array changing values to be total
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # sort into 
    sorted_arr = arr.copy()
    for i in range(0, len(arr)):
        sorted_arr[count_arr[arr[i]]-1] = arr[i]
        count_arr[arr[i]] -= 1
    print(sorted_arr)

    return sorted_arr

arr1 = [9, 5, 2, 0, 1, 6, 1, 5, 5]
arr2 = [0,3,4,2,5,1,6,8,7,9]
count_sort(arr2)
# print([1,1,2,5,5,5,6,9])
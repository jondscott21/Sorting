# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # TO-DO: swap
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

    return arr
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(arrA, arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a_idx = 0
    b_idx = 0
    for i in range(len(merged_arr)):
        if a_idx >= len(arrA) and b_idx >= len(arrB):
            return merged_arr
        elif a_idx >= len(arrA):
            merged_arr[i] = arrB[b_idx]
            b_idx += 1
        elif b_idx >= len(arrB):
            merged_arr[i] = arrA[a_idx]
            a_idx += 1
        elif arrA[a_idx] <= arrB[b_idx]:
            merged_arr[i] = arrA[a_idx]
            a_idx += 1
        else:
            merged_arr[i] = arrB[b_idx]
            b_idx += 1
    return merged_arr

# implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort, right_sort)

print(merge_sort([2,3,7,8,9,0,5,8,3]))
print([0,2,3,3,5,7,8,8,9])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

def partition(data):
    # making pivot a random choice is optimal
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)
    return left, [pivot], right

def quicksort(data):
    
    if len(data) <= 1:
        return data
    
    left, pivot, right = partition(data)

    return quicksort(left) + pivot + quicksort(right)

print(quicksort([2,3,7,8,1,9,0,5,8,3]))
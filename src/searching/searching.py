# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(len(arr)):
    if arr[i] == target:
      return i

  return -1   # not found
# print(linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], 0))


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  middle = (high - low) // 2
  for i in range(low, high):
    if target == arr[middle]:
      return middle
    elif target < arr[middle]:
      high = middle
      middle = (high - low) // 2
    else:
      low = middle
      middle = (high - low) // 2

  return -1 # not found

print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -9))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  middle = (low+high)//2
  if len(arr) == 0:
    return -1 # array empty
  # add missing if/else statements, recursive calls
  if target == arr[middle]:
    return middle
  if high == middle or low == middle:
    return None
  if target < arr[middle]:
    high = middle
    return binary_search_recursive(arr, target, low, high)
  else:
    low = middle
    return binary_search_recursive(arr, target, low, high)
bi_array = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search_recursive(bi_array, 1, 0, len(bi_array)-1))
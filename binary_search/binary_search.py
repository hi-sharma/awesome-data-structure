def search_or_insert_index(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return left
      
  
# sorted arr with duplicate elements
'''
1. Change with condition to <
2. Left update --> left = mid + 1
3. Right update --> right = left
4. equal update:
  a. Find left most element: Include with "Right update"
  b. Find right most element: Include with "Left update"
'''
def search_or_insert_left_index_duplicate(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
      # search in right subarr
      left = mid + 1
    elif arr[mid] >= target:
      # search in left subarr
      right = mid
  return left

def search_or_insert_right_index_duplicate(arr, target):
  left = 0
  right = len(arr) - 1
  while left < right:
    mid = (left + right) // 2
    if arr[mid] <= target:
      # search in right subarr
      left = mid + 1
      # search in left subarr
    elif arr[mid] > target:
      right = mid
  # rightmost index + 1
  return left

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
      
  

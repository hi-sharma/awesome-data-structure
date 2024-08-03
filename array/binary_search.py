# binary search in a sorted array in python
# Implement both ways: recursively and iteratively

def bst_recursive(arr, start_ind, end_ind, key):
    # base condition
    if end_ind < start_ind:
        return -1
    mid_ind = (start_ind + end_ind)//2
    if key == arr[mid_ind]:
        return mid_ind
    elif key < arr[mid_ind]:
        # search in left array
        return bst_recursive(arr, start_ind, mid_ind-1, key)
    else:
        # search in right array
        return bst_recursive(arr, mid_ind+1, end_ind, key)


def bst_iterative(arr, start_ind, end_ind, key):
    while end_ind >= start_ind:
        mid_ind = (start_ind + end_ind)//2
        if arr[mid_ind]==key:
            return mid_ind
        elif key < arr[mid_ind]:
            end_ind = mid_ind-1
        else:
            start_ind = mid_ind+1
        # import pdb; pdb.set_trace()  
    return -1

if __name__ == '__main__':
    array = [-1,2,5,6,7,9,12,19,21,4132]
    search_key = 22
    # array = input("Enter the sorted array, comma separated")
    # array = [int(i) for i in array.split(',')]
    # search_key = input('Enter search key')
    print("WARNING FROM IMPLEMENTATION: INDEXING. Since MID_IND is already checked, do mid_ind+1 or mid_ind-1 to avoid call stack errors!")
    search_result = bst_recursive(array, 0, len(array)-1, search_key)
    # search_result = bst_iterative(array, 0, len(array)-1, search_key)
    if search_result==-1:
        print(f"Key not found")
    else:
        print(f"key found at {search_result}")
    
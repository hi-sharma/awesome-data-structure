
def print_row_2Dmatrix(mat: List[List[*]]) -> List[]:
  for row in mat:
    print(row)

def print_col_2Dmatrix(mat: List[List[*]]) -> List[]:
  # get index in horizontal right direction for cols by iterating over first row
  for col in range(len(mat[0])):
    current_col = []
    # get index in vertical down direction for rows 
    for row in range(len(mat):
      current_col.append(mat[row][col])
    print(col)

def sum_linked_list(head):
  ans = 0
  while head:
    ans += head.val
    head = head.next
  return ans

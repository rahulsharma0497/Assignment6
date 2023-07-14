def search_matrix(matrix, target):
  """
  Returns True if target is in matrix, False otherwise.

  Args:
    matrix: A 2D array of integers.
    target: The target integer.

  Returns:
    True if target is in matrix, False otherwise.
  """

  m = len(matrix)
  n = len(matrix[0])
  i = 0
  j = n - 1
  while i < m and j >= 0:
    if matrix[i][j] == target:
      return True
    elif matrix[i][j] < target:
      i += 1
    else:
      j -= 1
  return False


if __name__ == "__main__":
  matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
  target = 3
  print(search_matrix(matrix, target))
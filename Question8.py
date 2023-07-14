def sparse_matrix_multiplication(mat1, mat2):
  """
  Returns the result of mat1 x mat2.

  Args:
    mat1: A sparse matrix of size m x k.
    mat2: A sparse matrix of size k x n.

  Returns:
    A sparse matrix of size m x n.
  """

  result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
  for i in range(len(mat1)):
    for j in range(len(mat2[0])):
      for k in range(len(mat2)):
        if mat1[i][k] != 0 and mat2[k][j] != 0:
          result[i][j] += mat1[i][k] * mat2[k][j]
  return result


if __name__ == "__main__":
  mat1 = [[1, 0, 0], [-1, 0, 3]]
  mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
  print(sparse_matrix_multiplication(mat1, mat2))
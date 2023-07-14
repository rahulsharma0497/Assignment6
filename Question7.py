def spiral_matrix(n):
  """
  Returns an n x n matrix filled with elements from 1 to n2 in spiral order.

  Args:
    n: A positive integer.

  Returns:
    An n x n matrix.
  """

  matrix = [[0 for _ in range(n)] for _ in range(n)]
  i, j, count = 0, 0, 1
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  while count <= n ** 2:
    matrix[i][j] = count
    count += 1
    d = directions[i % 4]
    i += d[0]
    j += d[1]
    if i < 0 or i >= n or j < 0 or j >= n or matrix[i][j] != 0:
      i -= d[0]
      j -= d[1]
      directions = directions[directions.index(d) + 1:] + directions[:directions.index(d)]
  return matrix


if __name__ == "__main__":
  n = 3
  print(spiral_matrix(n))
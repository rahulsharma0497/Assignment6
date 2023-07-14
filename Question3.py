def is_mountain_array(arr):
  """
  Returns True if arr is a valid mountain array, False otherwise.

  Args:
    arr: An array of integers.

  Returns:
    True if arr is a valid mountain array, False otherwise.
  """

  n = len(arr)
  if n < 3:
    return False

  increasing = True
  for i in range(1, n):
    if arr[i] < arr[i - 1]:
      increasing = False
      break

  if not increasing:
    for i in range(n - 2, 0, -1):
      if arr[i] < arr[i - 1]:
        return True

  return False


if __name__ == "__main__":
  arr = [2, 1]
  print(is_mountain_array(arr))
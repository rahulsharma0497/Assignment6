def original_array(changed):
  """
  Returns original if changed is a doubled array. If changed is not a doubled array, returns an empty array. The elements in original may be returned in any order.

  Args:
    changed: An array of integers.

  Returns:
    The original array.
  """

  n = len(changed) // 2
  original = []
  seen = set()
  for num in changed:
    if num in seen:
      return []
    else:
      seen.add(num)
      original.append(num)
      original.append(2 * num)
  return original


if __name__ == "__main__":
  changed = [1, 3, 4, 2, 6, 8]
  print(original_array(changed))
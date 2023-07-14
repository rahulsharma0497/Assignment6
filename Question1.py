def di_string_match(s):
  """
  Reconstructs the permutation perm from the string s.

  Args:
    s: A string representing the permutation perm.

  Returns:
    The permutation perm.
  """

  n = len(s)
  perm = []
  i = 0
  for c in s:
    if c == 'I':
      perm.append(i)
      i += 1
    else:
      perm.append(n - i - 1)
      i += 1
  return perm


if __name__ == "__main__":
  print(di_string_match("IDID"))
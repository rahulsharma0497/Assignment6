def max_len_equal_zero_one(nums):
  """
  Returns the maximum length of a contiguous subarray with an equal number of 0 and 1.

  Args:
    nums: A binary array.

  Returns:
    The maximum length of a contiguous subarray with an equal number of 0 and 1.
  """

  count_0 = 0
  count_1 = 0
  max_len = 0
  for num in nums:
    if num == 0:
      count_0 += 1
    elif num == 1:
      count_1 += 1

    if count_0 == count_1:
      max_len = max(max_len, count_0 + count_1)
    elif count_0 > count_1:
      count_0 = 0
    else:
      count_1 = 0
  return max_len


if __name__ == "__main__":
  nums = [0, 1]
  print(max_len_equal_zero_one(nums))
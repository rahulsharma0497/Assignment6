def min_product_sum(nums1, nums2):
  """
  Returns the minimum product sum if you are allowed to rearrange the order of the elements in nums1.

  Args:
    nums1: An array of integers.
    nums2: An array of integers.

  Returns:
    The minimum product sum.
  """

  n = len(nums1)
  sum1 = 0
  sum2 = 0
  for i in range(n):
    sum1 += nums1[i]
    sum2 += nums2[i]

  min_product_sum = float("inf")
  for i in range(n):
    new_sum1 = sum1 - nums1[i] + nums2[i]
    new_sum2 = sum2 - nums2[i] + nums1[i]
    min_product_sum = min(min_product_sum, new_sum1 * new_sum2)
  return min_product_sum


if __name__ == "__main__":
  nums1 = [5, 3, 4, 2]
  nums2 = [4, 2, 2, 5]
  print(min_product_sum(nums1, nums2))
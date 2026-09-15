nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

def unique(nums1, nums2):

    seen = set(nums1)
    added = set()
    result = []
    for num in nums2:
      if num in seen and num not in added:

        result.append(num)
        added.add(num)

    return result

print(unique(nums1, nums2))
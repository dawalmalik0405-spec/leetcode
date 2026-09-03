nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def Maximum_Subarray(nums):

  
  current = nums[0]
  best = nums[0]

  for i in nums[1:]:
      current = max(current + i, i )    
      best = max(best, current)

  return best

print(Maximum_Subarray(nums))


  

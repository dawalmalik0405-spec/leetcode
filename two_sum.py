nums = [2,  11, 15,7]
target = 9

seen = {}

def two_sum(nums, target):
  for i in range(len(nums)):

    needed = target - nums[i]
    if needed in seen:
      t = seen[needed]
      return(t, i)
    
    seen[nums[i]] = i


print(two_sum(nums, target))
    

    
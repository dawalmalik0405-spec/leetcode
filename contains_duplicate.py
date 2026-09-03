nums = [1, 2, 3, 1]




def conatins_duplicate(nums):
  seen = set()

  for i in nums:

    if i in seen:
      return True
    seen.add(i)


  return False

  


print(conatins_duplicate(nums))
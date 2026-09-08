nums = [0,1,2,4,5,6,7]

def minimum():
  left = 0
  right = len(nums) - 1



  while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
      left = mid + 1

    

    if nums[mid] < nums[right]:
      right = mid 

    
    
  return nums[left]
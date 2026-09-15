nums = [2,2,1]

def single_num(nums):

  answer = 0 

  for num in nums:
    answer ^= num
  return answer
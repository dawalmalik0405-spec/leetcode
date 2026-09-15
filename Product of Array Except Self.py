nums = [1, 2, 3, 4]

def product(nums):
  result = [1] * len(nums)
  left_product = 1

  for i in range(len(nums)):
      result[i] = left_product
      left_product *= nums[i]



  right_product = 1
  for j in range(len(nums)-1,-1,-1):
     result[j] = result[j] * right_product
     right_product = right_product*nums[j]


 

  return result

print(product(nums))



#   return result[::-1] 

# print(product(nums))
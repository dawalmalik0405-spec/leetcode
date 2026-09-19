nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

def unique(nums1, nums2):


  count = {}

  result = []

  for num in nums1:
    
    if num in count:
      count[num] += 1
    else:
      count[num] = 1

  for i in nums2:
    if i in count and count[i] > 0:

      result.append(i)

      count[i] -= 1

  return result


print(unique(nums1, nums2))


        

         
      
      

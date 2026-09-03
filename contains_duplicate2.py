class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):

            # What should we check here?
            if nums[i] in seen and i-seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
              
        return False
                

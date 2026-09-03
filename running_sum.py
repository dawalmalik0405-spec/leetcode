
nums = [1, 2, 3, 4]


class Solution(object):
    def runningSum(self, nums):
        result = []
        current_sum = 0

        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            result.append(current_sum)

        return result

s = Solution()

print(s.runningSum(nums))
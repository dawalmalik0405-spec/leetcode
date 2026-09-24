class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        greater = {}
        result = []

        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num

            stack.append(num)

        

        for num in nums1:
            result.append(greater.get(num, -1))

        return result
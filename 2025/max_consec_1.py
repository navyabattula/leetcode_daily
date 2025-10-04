"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Input: nums = [1,1,0,1,1,1]
Output: 3
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0

        max_count = max(max_count, current_count)

        return max_count


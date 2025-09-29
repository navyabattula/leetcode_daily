"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1


        for key in count:
            if count[key] != 2:
                return key



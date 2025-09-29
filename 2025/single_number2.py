"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

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
            if count[key] != 3:
                return key


        

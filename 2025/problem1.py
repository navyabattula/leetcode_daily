"""
Contains Duplicate
Solved
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 'True'
            elif i in hashMap:
                return True
        return False

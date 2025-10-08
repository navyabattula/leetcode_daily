"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(0, n):
            if target == nums[i]:
                return i
            elif i!= n-1 and nums[i]<target and target < nums[i+1]:
                return i+1
        if target < nums[0]:
            return 0
        elif target > nums[n-1]:
            return n

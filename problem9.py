"""
Binary Search
Solved 
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) //2
        while(low<=high):
            if target > nums[mid]:
                low = mid +1
                mid = (low + high) // 2
            elif target < nums[mid]:
                high = mid -1
                mid = (low + high) // 2
            elif target == nums[mid]:
                return mid
        return -1

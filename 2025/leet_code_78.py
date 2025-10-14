"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
    
        #subsets_rest = subsets(nums[1:])
        subsets_rest = Solution().subsets(nums[1:])
        subsets_with_first = [[nums[0]] + subset for subset in subsets_rest]
    
        return subsets_rest + subsets_with_first

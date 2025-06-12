"""
Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for i in hashSet:
            if i - 1 not in hashSet:
                j = i+1
                count = 1
                while j in hashSet:
                    j += 1
                    count += 1
                res = max(res, count)
        return res

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        k = 2

        while(k<len(nums)):
            if i<j<k and nums[i]<nums[j]<nums[k]:
                return True
            else:
                i += 1
                j += 1
                k += 1
        return False


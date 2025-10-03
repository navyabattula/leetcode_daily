"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Input: nums = [1,2,3,1], k = 3
Output: true
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            if num in window:
                return True
            window.add(num)

        return False


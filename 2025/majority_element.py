"""
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for key in count:
            if count[key] > (n//2):
                return key
        

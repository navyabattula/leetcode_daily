"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3 or len(set(nums))<3:
            return max(nums)
        else:
            set1 = set(nums)
            nums = list(set1)
            nums.sort(reverse=True)
            print(nums)
            return nums[2]


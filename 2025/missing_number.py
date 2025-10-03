"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [3,0,1]

Output: 2


"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = max(nums)
        compare = []
        for i in range(0, maxi+1):
            compare.append(i)
        for i in compare:
            if i not in nums:
                return i
        return maxi+1


"""
3Sum
Solved 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(0, len(nums)):
            j = i+1
            while(j<len(nums)):
                k = -(nums[i]+nums[j])
                if k in nums and nums.index(k) != j and nums.index(k) !=i:
                    ind = nums.index(k)
                    temp = [nums[i], nums[j], k]
                    flag =0
                    for x in res:
                        if x[0] in temp and x[1] in temp and x[2] in temp:
                           flag = 1
                           break
                    if flag == 0:
                        res.append(temp)
                     
                j+= 1
        return res
            

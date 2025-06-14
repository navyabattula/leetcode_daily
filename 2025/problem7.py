"""
Two Integer Sum II
Solved 
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            value = target - i
            if value in numbers and numbers.index(i)!= numbers.index(value):
                index1 = numbers.index(i)
                index2 = numbers.index(value)
                if index1 > index2:
                    return [index2+1, index1+1]
                else:
                    return [index1+1, index2+1]

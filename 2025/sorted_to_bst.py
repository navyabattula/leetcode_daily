"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        def convert(start, end):
            if start > end:
                return None
            mid = (start + end)//2

            root = TreeNode(nums[mid])

            root.left = convert(start, mid-1)

            root.right = convert(mid+1, end)

            return root

        return convert(0, len(nums)-1)


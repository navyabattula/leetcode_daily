"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while(x>0):
            rem = x%10 
            rev = rev *10 + rem
            x = x//10
        if temp == rev:
            return True 
        else:
            return False        

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x>2147483647 or x<-2147483648:
            return 0
        rev = 0
        sign =1
        if x<0:
            sign =-1
            x*=-1
        while x!=0:
            rem = int(x%10)
            rev = int(rev*10) + int(rem)
            x = int(x/10)
        if rev*sign>2147483647 or rev*sign<-2147483648:
            return 0
        return rev*sign

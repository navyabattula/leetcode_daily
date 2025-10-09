"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""
import math as m
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x>100.0 or x< -100.0:
            return 1.00
        elif n> 2147483647 or n< -2147483648:
            return 1.00
        else:
            p = m.pow(x,n)
            return p

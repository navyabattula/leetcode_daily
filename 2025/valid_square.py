"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while(low<=high):
            mid = (low+high)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1
            elif mid * mid < num:
                low = mid + 1
            mid = (low + high)//2
        return False

        

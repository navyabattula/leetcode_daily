"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        rev = 0
        rem = []
        for i in range(0,n):
            rev = digits[i] * pow(10, n-i-1) + rev
            print(rev)
        rev = rev + 1
        m = len(str(rev))
        for i in range(0, n):
            temp = rev//pow(10, n-i-1)
            if temp > 9:
                temp1 = temp//10
                rem.append(temp1)
                temp = temp%10
            rem.append(temp)
            rev = rev%pow(10,n-i-1)
        return rem

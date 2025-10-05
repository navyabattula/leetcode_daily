"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


"""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s1 = s1.lower()
        n = len(s1)
        first = 0
        last = n-1
        while(first<last):
            if s1[first] == s1[last]:
                first = first + 1
                last = last - 1
                continue
            elif s1[first] != s1[last]:
                return False
        return True
        

"""
Valid Palindrome
Solved 
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[\W_]+', '', s)
        start = 0
        end = len(s)-1
        while start<len(s) and end!=-1:
            if s[start] != s[end]:
                return False
            if start == end:
                break
            start += 1
            end -= 1
        return True

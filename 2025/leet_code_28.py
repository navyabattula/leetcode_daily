"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif needle not in haystack:
            return -1
        elif needle in haystack:
            for i in range(len(haystack)):
                for j in range(len(haystack), 0, -1):
                    temp = haystack[i:j]
                    if temp == needle:
                        return i

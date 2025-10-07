"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        n1 = len(word1)
        n2 = len(word2)
        flag = 0
        if n1<n2:
            for i in range(0,n1):
                merged += word1[i]
                merged += word2[i]
                
            merged += word2[n1:n2]
        elif n1>n2:
            for i in range(0,n2):
                merged += word1[i]
                merged += word2[i]
                
            merged += word1[n2:n1]
        else:
            for i in range(0,n1):
                merged += word1[i]
                merged += word2[i]
                
        return merged


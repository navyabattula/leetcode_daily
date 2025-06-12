"""
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        for i in s:
            if i not in hashMap1:
                hashMap1[i] = 1
            elif i in hashMap1:
                hashMap1[i] += 1

        for i in t:
            if i not in hashMap2:
                hashMap2[i] = 1
            elif i in hashMap2:
                hashMap2[i] += 1\
        
        if len(hashMap1) != len(hashMap2):
            return False
        else:
            for key in hashMap1:
                if key not in hashMap2:
                    return False
                if hashMap1[key] != hashMap2[key]:
                    return False 
            return True   
          

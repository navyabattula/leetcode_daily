"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        p1 = 0
        p2 = len(s) - 1
        temp_list = list(s)
        while(p1<=p2):
            if temp_list[p1] in vowels and temp_list[p2] in vowels:
                temp = temp_list[p1]
                temp_list[p1] = temp_list[p2]
                temp_list[p2] = temp
                p1 += 1
                p2 -= 1
            elif temp_list[p1] in vowels and temp_list[p2] not in vowels:
                p2 -= 1
            elif temp_list[p1] not in vowels and temp_list[p2] in vowels:
                p1 += 1
            elif temp_list[p1] not in vowels and temp_list[p2] not in vowels:
                p2 -= 1
                p1 += 1
        str1 = "".join(temp_list)
        return str1



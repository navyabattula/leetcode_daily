"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        char_list = s.split()
        p1 = 0
        p2 = len(char_list) - 1
        while(p1<=p2):
            temp = char_list[p1]
            char_list[p1] = char_list[p2]
            char_list[p2] = temp
            p1 += 1
            p2 -= 1
        return " ".join(char_list)


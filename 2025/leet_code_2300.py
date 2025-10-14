"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.


"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        ans = []

        for spell in spells:
            idx = self.bs(potions, spell, success)
            ans.append(len(potions) - idx if idx != -1 else 0)
        return ans

    def bs(self, potions, strength, success):
        low, high = 0, len(potions) - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if potions[mid] * strength >= success:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        return idx        

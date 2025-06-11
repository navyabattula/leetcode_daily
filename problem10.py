"""
Best Time to Buy and Sell Stock
Solved
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        res = 0
        n = len(prices)
        l, r = 0, 1
        while(r <n):
            if prices[l] < prices[r]:
                res = prices[r] - prices[l]
            else:
                l = r
            r = r + 1
            maxProf = max(maxProf, res)
        return maxProf


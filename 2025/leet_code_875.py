"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


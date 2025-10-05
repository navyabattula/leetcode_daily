"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (low+high)//2

        while (low<=high):
            x = guess(mid)
            if  x == 0:
                return mid
            elif x == -1:
                high = mid -1
            elif x == 1:
                low = mid + 1
            mid = (low + high)//2


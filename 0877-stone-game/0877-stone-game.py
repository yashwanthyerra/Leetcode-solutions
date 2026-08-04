from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i, j):
          
            if i == j:
                return piles[i]

            takeLeft = piles[i] - dp(i + 1, j)
            takeRight = piles[j] - dp(i, j - 1)

            return max(takeLeft, takeRight)

        return dp(0, len(piles) - 1) > 0
        
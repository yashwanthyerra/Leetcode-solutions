class Solution:
    def climbStairs(self, n: int) -> int:

        # memo = {1:1,2:2}

        # def climb(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = climb(n-1) + climb(n-2)
        #         return memo[n]
        # return  climb(n)
        

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
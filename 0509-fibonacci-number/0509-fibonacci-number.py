class Solution:
    def fib(self, n: int) -> int:

        memo = {0:0,1:1}

        def fibb(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = fibb(x-1) + fibb(x-2)

                return memo[x]
        return fibb(n)

        
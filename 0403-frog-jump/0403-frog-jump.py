class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones)==2:
            if stones[-1]==1:
                return True
            return False
        n = len(stones)
        dp = [set() for i in range(n)]
        dp[0].add(0)
        pos = {stones[i]: i for i in range(n)}
        for i in range(n):

            for k in dp[i]:
                #k-1
                if k-1>0 and stones[i] + k-1 in pos:
                    j = pos[stones[i] + k-1]
                    dp[j].add(k-1)
                #k
                if  stones[i] + k in pos:
                    j = pos[stones[i] + k]
                    dp[j].add(k)
                #k+1
                if stones[i] + k+1 in pos:
                    j = pos[stones[i] + k+1]
                    dp[j].add(k+1)

        return len(dp[-1])>0

         
            

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones)<=2:
            return max(stones)
        l = []

        for i in range(0,len(stones)-2):
            l.append(stones[i+2]-stones[i])    


        return max(l)    
class Solution:
    def rob(self, nums: List[int]) -> int:
        cost = nums
        n = len(cost)
    
        cost.append(0)
        for i in range(n-3,-1,-1):
            cost[i] = cost[i]+max(cost[i+2],cost[i+3])

        return max(cost[0],cost[1])
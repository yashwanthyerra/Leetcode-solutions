class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        def can_partition(arr,indx,target,dp):
            n = len(arr)

            if target == 0:
                return True
            
            if indx == n:
                return False

            if dp[indx][target] != -1:
                return dp[indx][target]

            if target - arr[indx] >=0:
                pick = can_partition(arr,indx+1,target-arr[indx],dp)

                if pick == True:
                    dp[indx][target] = True
                    return True

            not_pick =  can_partition(arr,indx+1,target,dp)

            dp[indx][target] = not_pick

            return not_pick

        def knapsack(arr):
            n = len(arr)

            if sum(arr) % 2 != 0:
                return False
            target = sum(arr)//2

            dp = [[-1]*(target+1) for _ in range(n)]

            return can_partition(arr,0,target,dp)

        return knapsack(nums)
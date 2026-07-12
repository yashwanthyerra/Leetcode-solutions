class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        window_sum = nums[0]
        max_sum = window_sum
        

        for i in range(1,len(nums)):
            new_sum = max(nums[i],nums[i]+window_sum)

            max_sum = max(max_sum,new_sum)

            window_sum = new_sum

        return max_sum

            

            









        
          
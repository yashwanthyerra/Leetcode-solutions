class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   
        
        for i in range(len(nums)):
    
            y= target-nums[i]
        
            if y in nums[i+1::]:
                return(i,nums[i+1::].index(y)+1+i)

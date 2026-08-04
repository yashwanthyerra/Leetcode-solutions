class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        result = []
        for i in range(1,len(nums)):
            if nums[i-1]+1 != nums[i]:
                result.extend([x for x in range(nums[i-1]+1,nums[i])])


        return result
        

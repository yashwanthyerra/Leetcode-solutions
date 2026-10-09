class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 2:
            return 1 if nums[1] >= nums[0] else 0
        if len(nums) == 1:
            return 0

        n = len(nums)
        
        left = 0 
        right = 2
        found = False
        for i in range(1,n):
            if  right < n and nums[i] > nums[left] and nums[i] > nums[right]:
                return (left+right)//2

            elif nums[0] > nums[1]:
                return 0
            elif nums[-1] > nums[-2]:
                return len(nums)-1

            else:
                if right < n:
                    left+=1
                    right+=1

                else:
                    break
        
        return 0
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        n = len(nums)
        temp = nums[::-1]
        nums.append(0)
        
        for i in range(n-3,-1,-1):
            x= max(nums[i+2],nums[i+3])
            nums[i] = nums[i]+max(nums[i+2],nums[i+3])
        
        x1 = max(nums[0],nums[1])

        temp.append(0)
        for i in range(n-3,-1,-1):
            x= max(temp[i+2],temp[i+3])
            temp[i] = temp[i]+max(temp[i+2],temp[i+3])
        
        y1 = temp[0]

        if nums[0]<nums[1]:
            return nums[1]

        else:
            if x1==y1:
                nums[0] = nums[0]-nums[-2]

            return max(max(nums),temp[1])

            
            





        


            

        
        
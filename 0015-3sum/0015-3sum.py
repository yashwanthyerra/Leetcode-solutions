class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        n = len(nums)
        used = {}
        result = []
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left  = i+1
            right = n-1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    l=[]
                    l.append(nums[left])
                    l.append(nums[right])
                    l.append(nums[i])
                    l = sorted(l)
                    key = tuple(l)
                    if key not in used:
                        result.append(l)
                        used[key] = True
                    left+=1
                    right-=1
                elif  nums[left] + nums[right] < -nums[i]:
                    left+=1
                else:
                    right-=1
        return result
                
       
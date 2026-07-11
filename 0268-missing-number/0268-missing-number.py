class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        l = [x for x in range(0,len(nums)+1)]
        r =[]
        for i in l:
            if i not in nums:
                r.append(i)

        return r[0]
                
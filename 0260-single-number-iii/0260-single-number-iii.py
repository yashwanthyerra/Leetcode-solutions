from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        freq = Counter(nums)
        result=[]

        for key,value in freq.items():
            if value==1:
                result.append(key)


        return result
        
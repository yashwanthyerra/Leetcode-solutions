from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        freq = Counter(nums)
        for key,value in freq.items():
            if value==1:
                return key



        
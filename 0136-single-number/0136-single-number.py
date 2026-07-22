from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        freq = Counter(nums)
        for i in freq:
            if freq[i]==1:
                return i

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums = sorted(nums)

        if len(nums) < 2:
            return 0

        r = []

        for i in range(1, len(nums)):
            r.append(nums[i] - nums[i-1])

        y = max(r)
        return y
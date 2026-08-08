class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_end = 0
        far = 0

        for i in range(len(nums)-1):
            far = max(far,i+nums[i])

            if i==curr_end:
                curr_end = far

        return curr_end>=len(nums)-1
        
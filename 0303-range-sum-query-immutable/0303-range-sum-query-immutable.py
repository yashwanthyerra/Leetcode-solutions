class NumArray:

    def __init__(self, nums: List[int]):

        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:

        
        prefix_arr = [0]*len(self.nums)

        prefix_arr[0] = self.nums[0]

        for i in range(1,len(self.nums)):
            prefix_arr[i] = prefix_arr[i-1] + self.nums[i]


        if left==0:
            return prefix_arr[right]
        else:
            return prefix_arr[right]-prefix_arr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
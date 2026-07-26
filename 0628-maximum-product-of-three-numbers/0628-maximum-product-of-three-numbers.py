def quicksort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    pivot= arr[mid]
    left = [x for x in arr if x>pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x<pivot]
    return quicksort(left) + mid + quicksort(right)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = quicksort(nums)
    
        return max((nums[0]*nums[1]*nums[2]),(nums[0]*nums[-1]*nums[-2]))

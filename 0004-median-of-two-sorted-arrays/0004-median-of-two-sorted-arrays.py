def merge(left,right):

    result =[]
    i = 0
    j = 0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = merge(nums1,nums2)
        if len(nums) ==1:
            return nums[0]
        if len(nums)<1:
            return 0

        if len(nums)%2 !=0:
            return nums[len(nums)//2]
        
        else:
            return (nums[len(nums)//2] + nums[(len(nums)//2)-1])/2

        

        

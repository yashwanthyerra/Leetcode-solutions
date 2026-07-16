def quick_sort(arr):

    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    pivot = arr[mid]

    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]

    return quick_sort(left) + mid + quick_sort(right)

def gcd(a,b):
    if b==0:
        return a

    if b>a:
        a,b = b,a

    return gcd(b,a%b)

class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        max_ele = nums[0]

        prefix_gcd =[]

        for i in range(len(nums)):

            max_ele = max(max_ele,nums[i])
            prefix_gcd.append(gcd(nums[i],max_ele))


        prefix_gcd = quick_sort(prefix_gcd)

        
        result = 0
        for i in range(len(nums)//2):
            result += gcd(prefix_gcd[i],prefix_gcd[len(nums)-i-1])


        return result



        
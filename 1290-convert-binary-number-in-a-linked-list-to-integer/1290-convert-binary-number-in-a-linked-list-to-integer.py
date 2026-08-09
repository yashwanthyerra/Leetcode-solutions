# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def convert_to_binary(nums):
    
    i = 0
    result = 0
    nums = nums[::-1]
    while i<len(nums):
        result += nums[i]*(2**i)
        i+=1

    return result


    

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        nums = []

        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        result = convert_to_binary(nums)

        return result

        
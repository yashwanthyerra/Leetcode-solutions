# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def quick_sort(arr):

    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    pivot = arr[mid]

    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]

    return quick_sort(left) + mid + quick_sort(right)

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        nums =[]
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        new = quick_sort(nums)

        nodes = [ListNode(x) for x in new]

        for i in range(len(new)-1):
            nodes[i].next = nodes[i+1]

        if not nodes:
            return None
        head = nodes[0]
        return head
            

        
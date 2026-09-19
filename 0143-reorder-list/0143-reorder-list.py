# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse(head):
    if not head:
        return None
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
            
        c = 0
        curr = head

        while curr:
            curr = curr.next
            c+=1
        n = (c+1)//2
        i = 0
        curr2 = head

        while i < n-1:
            curr2 = curr2.next
            i+=1
        right = curr2.next
        curr2.next = None

        right = reverse(right)

        curr2 = head
       
    
        while right:
            store = right.next
            next_left = curr2.next
            right.next  = next_left
            curr2.next = right
            curr2  = next_left

            right = store
            










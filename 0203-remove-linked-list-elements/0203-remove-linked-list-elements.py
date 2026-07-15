# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head and head.val==val:
            head = head.next

        if head is None :
            return head

        prev = head
        curr = head.next

        while curr :   
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
                continue

            prev = curr
            curr = curr.next

        return head

                        

            




            
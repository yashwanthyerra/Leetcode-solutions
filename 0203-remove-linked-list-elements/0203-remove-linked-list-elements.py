# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        # if all are vals like (7 --> 7 --> 7)
        while head and head.val==val:
            head = head.next

        if head is None :
            return head

        dummy = ListNode(0)
        curr1 = dummy
        curr = head

        while curr :   
            if curr.val != val:
                curr1.next = curr
                curr1 = curr1.next
                curr = curr.next
            else:
                curr1.next = curr.next
              
                curr = curr.next

        return dummy.next

                        

            




            
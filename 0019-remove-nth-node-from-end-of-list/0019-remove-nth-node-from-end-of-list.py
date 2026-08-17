# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None :
            return
        if head.next is None:
            head = None
            return head

        temp  = head
        curr = head
        x = 0
        while temp:
            x+= 1
            temp= temp.next

        y = x-n
        N = 0

        if y==0:
            head = head.next
            
        while curr and N<y-1:

            N+=1

            curr = curr.next

        curr.next = curr.next.next


        return head

        




        
        
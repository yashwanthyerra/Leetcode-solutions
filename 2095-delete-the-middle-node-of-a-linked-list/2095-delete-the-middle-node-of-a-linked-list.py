# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def len_LL(head):
    if head is None :
        return 0
    curr = head
    count = 0
    while curr:
        count+= 1
        curr = curr.next
    return count

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 

        if len_LL(head) == 1 :
            head = None
            return head

        elif len_LL(head) == 2 :
            head.next = head.next.next
            return head

        else:

            length = len_LL(head)//2

            curr =head

            count = 1

            while count < length:
                count+=1
                curr = curr.next

            curr.next = curr.next.next

        return head


        
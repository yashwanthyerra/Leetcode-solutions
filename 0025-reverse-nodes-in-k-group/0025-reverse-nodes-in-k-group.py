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
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head :
            return None
        length = 0
        current = head
        while current:
            current = current.next
            length +=1

        if length < k:
            return head

        dummy  = ListNode(0)
        curr = dummy

        did  = 0
        while did+k <= length:
            i = 1
            curr2 = head
            group_start = curr2
            while i<k and curr2:

                curr2 = curr2.next
                i+=1
            curr3 = curr2.next
            curr2.next = None
            curr.next = reverse(group_start)
            curr = group_start
            head = curr3
            did += k

            curr.next = head
    

        return dummy.next

        

            
            

    
        

        

        


        
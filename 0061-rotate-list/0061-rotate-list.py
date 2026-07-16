# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        lenght = 1
        curr = head
        while curr.next:
            lenght +=1
            curr = curr.next
        # Reduce unnecessary rotations
        k %= lenght

        if k==0:
            return head

        # Make the list circular
        curr.next = head

        # find the new tail
        curr =  head
        for i in range(lenght-k-1):
            curr = curr.next
        # new head 
        new_head = curr.next
        # break the cycle
        curr.next = None

        return new_head
        

        
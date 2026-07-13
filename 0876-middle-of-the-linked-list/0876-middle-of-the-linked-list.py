# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_y(head):
    count =0
    current = head
    while current:
        count+=1
        current=current.next
    return count   

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if count_y(head)% 2 ==0:
            for i in range(count_y(head)//2):
                head = head.next
        else:
            for i in range((count_y(head)//2)):
                head = head.next
        
        return head
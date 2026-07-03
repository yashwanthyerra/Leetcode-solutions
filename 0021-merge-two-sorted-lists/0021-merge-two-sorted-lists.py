

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        current1 = list1
        current2 = list2
        
        if list1.val<=list2.val:
            head = list1
            prev =current1 
            current1 =current1.next
        else:
            head = list2
            prev = current2
            current2 = current2.next
        while current1 and current2: 
            if current1.val <=current2.val:
                prev.next = current1
                prev = current1
                current1 = current1.next
            else:
                prev.next = current2
                prev = current2
                current2 = current2.next

        if current1:
            prev.next =current1
        elif current2:
            prev.next = current2
        return head

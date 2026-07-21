# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_linked_lists(left,right):
    if left is None:
        return right
    if right is None:
        return left
    dummy = ListNode(0)
    curr  = dummy
    while left and right:
        if left.val<right.val:
            curr.next = left
            left = left.next
            curr= curr.next
        else:
            curr.next =  right
            right = right.next
            curr = curr.next

    if left:
        curr.next = left
    else:
        curr.next = right

    return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return None
        y = lists[0]
        for i in  range(1,len(lists)):
           y =  merge_linked_lists(lists[i],y)

        return y        

        
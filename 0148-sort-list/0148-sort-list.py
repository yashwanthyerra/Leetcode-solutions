# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_sort(head):
            if head is None or head.next is None:
                return head
            slow =head
            fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None # spliting 

            left = merge_sort(head)
            right = merge_sort(slow)

            return merge(left,right)

        def merge(left,right):

            dummy = ListNode(0)

            curr = dummy

            while left and right:
                if left.val<right.val:
                    curr.next = left
                    left = left.next
                    curr = curr.next
                else:
                    curr.next = right
                    right = right.next
                    curr = curr.next

                
            if left:
                curr.next = left

            else:
                curr.next= right

            return dummy.next

        return merge_sort(head)






        
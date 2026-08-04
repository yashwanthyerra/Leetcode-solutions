class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = []
        curr1 = l1

        while curr1:
            r1.append(str(curr1.val))
            curr1 = curr1.next

        r2 = []
        curr2 = l2

        while curr2:
            r2.append(str(curr2.val))
            curr2 = curr2.next
        r1 = r1[::-1]
        r2 = r2[::-1]
        u = int("".join(r1))
        v = int("".join(r2))

        w = u + v

        lists = []
        if w == 0:
            lists.append(0)
        else:
            while w > 0:
                lists.append(w % 10)
                w //= 10

        nodes = [ListNode(x) for x in lists]

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        head = nodes[0]

        return head
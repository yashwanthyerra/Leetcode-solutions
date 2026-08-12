# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def in_order(root):
            if not root:
                return []

            return in_order(root.left) + [root.val] + in_order(root.right)


        l = in_order(root)

        freq = Counter(l)

        max_value = 0
        max_key = 0
        
        for key,value in freq.items():
            if value>max_value:
                max_value = value
            

        l = []

        for key,value in freq.items():
            if freq[key]==max_value:
                l.append(key)

        return l

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_order(node):
            if not node:
                return []
            
            return  in_order(node.left) +[node.val] + in_order(node.right)
        return in_order(root)
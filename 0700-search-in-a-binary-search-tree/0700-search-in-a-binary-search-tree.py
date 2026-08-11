# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_node(node,target):
            if not node:
                return None
            if node.val==target:
                return node
            if target<node.val: return search_node(node.left,target)
            else: return search_node(node.right,target)
        return search_node(root,val)

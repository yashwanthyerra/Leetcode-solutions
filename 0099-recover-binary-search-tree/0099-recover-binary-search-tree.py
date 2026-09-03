# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes= []
        def inorder_traversal(root):
            if not root:
                return 
            inorder_traversal(root.left)
            nodes.append(root)
            inorder_traversal(root.right)

        inorder_traversal(root)
        values = sorted(node.val for node in nodes)

        for node,value in zip(nodes,values):
            node.val = value






        
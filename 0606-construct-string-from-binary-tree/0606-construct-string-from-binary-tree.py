# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        s = str(root.val)
        if root.left is None and root.right is None:
            return str(root.val)

        if root.right and root.left:
            left = self.tree2str(root.left)
            right = self.tree2str(root.right)
            return str(f"{root.val}({left})({right})")

        if root.right and root.left is None:
            
            right = self.tree2str(root.right)
            return str(f"{root.val}()({right})")

        if root.left and root.right is None:
            left = self.tree2str(root.left)
            return str(f"{root.val}({left})")

        return s        
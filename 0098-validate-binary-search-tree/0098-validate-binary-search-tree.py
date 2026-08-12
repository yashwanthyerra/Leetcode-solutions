# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def in_order(root):
    if not root:
        return []
    
    return in_order(root.left) + [root.val] + in_order(root.right)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

     
        l = in_order(root)
        l2 = sorted(l)
        if len(set(l))==1 and len(l)>1:
            return False

        for i in range(1,len(l)):
            if l[i-1]>= l[i]:
                return False
        return True

        
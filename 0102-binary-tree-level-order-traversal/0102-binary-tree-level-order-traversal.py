# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result=[]

        while queue:
            l=[]
            size = len(queue)
            for i in range(size):

                root = queue.popleft()
                l.append(root.val)
                
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
        
            result.append(l)
        
        return result

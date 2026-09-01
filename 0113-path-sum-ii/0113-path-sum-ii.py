# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        l = []

        def dfs(root,r):
            if root is None:
                return 
            nonlocal l
                 
            r.append(root.val)

            if not root.left and not root.right:
                l.append(r.copy())

            dfs(root.left,r)
            dfs(root.right,r)

            r.pop()

        dfs(root,[])
        
        result = [i for i in l if sum(i)==targetSum]
        return result


        

            




        
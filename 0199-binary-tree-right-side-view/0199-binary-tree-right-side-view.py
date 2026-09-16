# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # if not root:
        #     return []

        # stk = [(root,0)]
        # result1 = []#op
        # result2 = []#store depths

        # while stk:
        #     node,dpt = stk.pop()

        #     if node.left:
        #         stk.append((node.left,dpt+1))

        #     if node.right:
        #         stk.append((node.right,dpt+1))

        #     if dpt not in result2:
        #         result1.append(node.val)    

        #     result2.append(dpt)
            
        # return result1

    # recursively
        result = []
        dp = []

        def dfs(root,depth):
            nonlocal result

            if not root:
                return 

            if depth not in dp:
                result.append(root.val)
            dp.append(depth)
            dfs(root.right,depth+1)
            dfs(root.left,depth+1)
            
            
        dfs(root,0)

        return result

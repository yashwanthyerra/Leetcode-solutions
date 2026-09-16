# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

       

        stk = [(root,1)]
        freq = {}
        result2 = [(root.val,1)]
        while stk:
            node,dpt = stk.pop()

            if node.left:
                stk.append((node.left,dpt+1))

            if node.right:
                stk.append((node.right,dpt+1))

           
            result2.append((node.val,dpt))
            
        
        for node,lvl in result2:

            if lvl in freq:
                freq[lvl] += node

            else:
                freq[lvl] = node

        max_ele = root.val
        max_key = 1

        for key,val in freq.items():
            if max_ele < val:
                max_ele = val
                max_key = key

        return max_key

            
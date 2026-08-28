# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        curr_max = root.val
        def dfs(root,curr_max):
            nonlocal count

            if not root:
                return 
            
            if root.val >= curr_max:
                count+=1

            curr_max = max(curr_max,root.val)

            dfs(root.left,curr_max)
            dfs(root.right,curr_max)

        dfs(root,curr_max)
        return count
    


















        # if root is None :
        #     return 0
        # stk = [root]
        # good_count = 1
        # curr_max = root.val
        # while stk:
            
        #     root = stk.pop()
            
        #     if root.left:
        #         stk.append(root.left)
        #         if root.left.val >= curr_max:
        #             good_count += 1
        #             curr_max = max(curr_max,root.left.val)
        #     if root.right:
        #         stk.append(root.right)
        #         if root.right.val >= curr_max:
        #             good_count +=1
        #             curr_max = max(curr_max,root.right.val)

        # return good_count
        
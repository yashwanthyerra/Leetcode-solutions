# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        needs_cameras =1
        has_cameras =2
        covered = 3
        placed_cameras = 0
                
        def dfs(root):
           
            nonlocal placed_cameras

            if not root :
                return covered

            left = dfs(root.left)
            right = dfs(root.right)

            if left ==needs_cameras or right ==needs_cameras:
                placed_cameras+=1
                return has_cameras

            if left==has_cameras or right==has_cameras:
                return covered
            
            return needs_cameras

        if dfs(root)==needs_cameras:
            placed_cameras+=1

        return placed_cameras




        

        
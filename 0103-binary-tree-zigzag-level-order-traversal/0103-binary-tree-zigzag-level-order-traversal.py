# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []

        q = [root]
        result = [[root.val]]
        level = 1
        while q:
            res = []

            for i in  range(len(q)):
                node = q.pop(0)

                if node.left:
                    res.append(node.left.val)
                    q.append(node.left)

                if node.right:
                    res.append(node.right.val)
                    q.append(node.right)
            if res:
                if level % 2:
                    result.append(res[::-1])
                else:
                    result.append(res)

            level += 1

        return result
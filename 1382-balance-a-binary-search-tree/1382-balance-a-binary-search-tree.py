# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Avl:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        t = x.right

        x.right = y
        y.left = t

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left

        y.left = x
        x.right = t

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, val):
        if root is None:
            node = TreeNode(val)
            node.height = 1
            return node

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        bf = self.balance(root)

        if bf > 1 and val < root.left.val:
            return self.right_rotate(root)

        if bf < -1 and val > root.right.val:
            return self.left_rotate(root)

        if bf > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if bf < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

class Solution:
    def inorder(self, root, arr):
        if root is None:
            return

        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        arr = []
        self.inorder(root, arr)

        tree = Avl()
        node = None

        for val in arr:
            node = tree.insert(node, val)

        return node
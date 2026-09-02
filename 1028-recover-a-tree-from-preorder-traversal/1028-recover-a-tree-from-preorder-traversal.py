# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []

        i = 0
        while i < len(traversal):

            count = 0

            while i <len(traversal) and  traversal[i] == "-":
                count+=1
                i+=1

            value = ""
            while i < len(traversal) and traversal[i].isdigit(): 
                value += traversal[i]
                i += 1

            if value:
                nodes.append((value,count))

        def buildtree(nodes):
            
            root = TreeNode(int(nodes[0][0]))
            stk = [(root,nodes[0][1])]


            for values,height in nodes[1:]:
                node = TreeNode(int(values))

                while stk and stk[-1][1] >= height:

                    stk.pop()

                parent = stk[-1][0]

                if parent.left is None:
                    parent.left = node

                else:
                    parent.right = node

                stk.append((node,height))

            return root

        return buildtree(nodes)

        

        

                    


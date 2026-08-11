# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder_successor(root):
    curr = root.right
    while curr.left:
        curr = curr.left
    return curr

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # searching the key 
        def del_Node(root,key):
            if root is None:
                return None
            curr = root
            parent = None
           
            while curr:
                if curr.val == key:
                    break
                parent = curr

                if curr.val<key:
                    curr = curr.right
                else:
                    curr = curr.left
            if curr is None:
                return root

            # node is leaf
            if curr.right == None and curr.left == None :
                if parent is None:
                    return None
                if parent.left==curr:
                    parent.left = None
                else:
                    parent.right = None
            if parent is None:
           # Root node deletion
                

                    if curr.left is None and curr.right is None:
                        return None

                    elif curr.left is None:
                        return curr.right

                    elif curr.right is None:
                        return curr.left

                    else:
                        successor = inorder_successor(curr).val
                        curr.val = successor
                        curr.right = del_Node(curr.right, successor)
                        return curr
            # node having one child
            elif curr.right is None or curr.left is None:

                if parent.left==curr:
                    if curr.left== None:
                        parent.left = curr.right
                    else:
                        parent.left =curr.left

                elif parent.right==curr:
        
                    if curr.left== None:
                        parent.right = curr.right
                    else:
                        parent.right=curr.left
            # NODE having 2 child
            else:
                successor = inorder_successor(curr).val
                curr.val = successor
                curr.right = del_Node(curr.right,successor)

            return root
        return del_Node(root,key)

            
                



                     
            

            
            
        

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def insert(root,key):
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert(root.left,key)
    elif key > root.val:
        root.right = insert(root.right,key)

    return root
from itertools import permutations
def same_tree(a,b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.val==b.val and same_tree(a.left,b.left) and same_tree(a.right,b.right))
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:


        result = []
        arr = [i for i in range(1,n+1)]
        x  = list(permutations(arr))
        
        for values in x:
            root = None
            for value in values:
                root = insert(root,value)
            is_new = True
            for tree in result:
                if same_tree(tree,root):
                    is_new = False
                    break
            if is_new:
                result.append(root)


        return result




        
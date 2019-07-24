# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def sumLeft(node,isLeft):
            if not node: return 0
            if node and isLeft and not node.left and not node.right:
                    return node.val
            
            return sumLeft(node.left,True) + sumLeft(node.right,False)
        
        return sumLeft(root, False)
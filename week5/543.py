# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxLength = 0
        
        def calc(node,prev):
            if not node: return 0
            
            left = calc(node.left,node)
            right = calc(node.right,node)
            self.maxLength = max(self.maxLength, left + right)
            
            return 1 + max(left,right)
        
        calc(root,None)
        return self.maxLength
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.maxLength = 0
        def traverse(node, prev):
            if not node: return 0
            left = traverse(node.left, node)
            right = traverse(node.right, node)
            self.maxLength = max(self.maxLength,left + right)
            return 1 + max(left,right) if prev and node.val == prev.val else 0
         
        traverse(root,None)
        return self.maxLength
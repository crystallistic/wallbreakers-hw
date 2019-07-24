# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        list1, list2 = [], []
        
        def preorderLeaf(node,nodeList):
            if not node: return 
            if not node.left and not node.right:
                nodeList.append(node.val)
            preorderLeaf(node.left,nodeList)
            preorderLeaf(node.right,nodeList)
        
        preorderLeaf(root1, list1)
        preorderLeaf(root2, list2)
        return list1 == list2
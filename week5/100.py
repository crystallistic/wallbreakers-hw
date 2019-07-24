# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        list1, list2 = [],[]
        def traverse(node, nodeList):
            if not node: 
                nodeList.append(None)
                return
            nodeList.append(node.val)
            traverse(node.left,nodeList)
            traverse(node.right, nodeList)
        traverse(p,list1)
        traverse(q,list2)
        return list1 == list2
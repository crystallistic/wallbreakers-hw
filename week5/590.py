"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.traverse(root,ans)
        return ans
    
    def traverse(self,node,nodeList):
        if not node:
            return 
        
        for child in node.children:
            self.traverse(child,nodeList)
            
        nodeList.append(node.val)
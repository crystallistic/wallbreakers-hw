# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def traverse(node,depth, leftScore, lookup):
            if not node: return 
            if depth not in lookup:
                lookup[depth] = []
            lookup[depth].append((node.val,leftScore))
                
            traverse(node.left,depth+1,leftScore+1,lookup)
            traverse(node.right,depth+1,leftScore-1,lookup)
        
        lookup = dict()
        traverse(root,0,0,lookup)
        
        print(lookup)
        maxDepth = max(lookup.keys())
        maxVal,maxScore = -math.inf, -math.inf
        for val,score in lookup[maxDepth]:
            if score > maxScore:
                maxScore = score
                maxVal = val
        return maxVal

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    
    print(sol.findBottomLeftValue(root))
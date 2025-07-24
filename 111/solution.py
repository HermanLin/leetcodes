from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # depth-first search solution
        def dfs(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)
        
            if node.left and node.right:
                return 1 + min(left, right)

            if node.left:
                return 1 + left
            
            return 1 + right

        return dfs(root)



sol = Solution() 

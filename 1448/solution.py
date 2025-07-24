from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''# recursive implementation
        def dfs(node: Optional[TreeNode], maxSoFar: float) -> int:
            if not node:
                return 0

            check = 1 if node.val >= maxSoFar else 0
            
            if not node.left and not node.right:
                return check 
        
            maxSoFar = max(maxSoFar, node.val)
            return check + dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)

        return dfs(root, float('inf'))'''

        # iterative implementation
        stack = [(root, float('-inf'))]
        count = 0

        while stack:
            node, maxSoFar = stack.pop()

            if node.val >= maxSoFar:
                count += 1

            maxSoFar = max(maxSoFar, node.val)
            if node.left:
                stack.append((node.left, maxSoFar))
            if node.right:
                stack.append((node.right, maxSoFar))

        return count
 
sol = Solution() 

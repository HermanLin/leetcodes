from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        '''if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # p and q are decendants of root
            return root

        if not left and not right:
            return None

        if left: 
            return left

        return right'''
        
        # improved solution, reduce complexity
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            return left if left else right
        
        return dfs(root)
 
sol = Solution() 

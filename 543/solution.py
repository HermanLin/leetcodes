from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        # diameter of a node is the left height + right height
        # height of a node is 1 + maximum between left and right heights
        def height(node: Optional[TreeNode], maxDiameter: int) -> Tuple[int, int]:
            if not node:
                return (0, 0)
            
            left_height, left_dia = height(node.left, maxDiameter)
            right_height, right_dia = height(node.right, maxDiameter)
            
            node_height = 1 + max(left_height, right_height)
            node_diameter = left_height + right_height
            max_diameter = max(maxDiameter, node_diameter, left_dia, right_dia)
            
            return (node_height, max_diameter)
            
        _, tree_diameter = height(root, 0)
        
        return tree_diameter
        '''

        # improved solution, 
        # reduce complexity by tracking diameter outside of helper
        diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)
            
            node_diameter = left_height + right_height
            diameter = max(diameter, node_diameter)

            return 1 + max(left_height, right_height)

        height(root)
        return diameter
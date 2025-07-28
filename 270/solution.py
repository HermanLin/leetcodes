
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        queue = deque([root])
        closestValue = int(float('inf'))
        
        while queue:
            node = queue.popleft()
            
            newClosestValue = abs(node.val - target)
            if newClosestValue < abs(closestValue - target):
                closestValue = node.val
            elif newClosestValue == abs(closestValue - target):
                closestValue = min(closestValue, node.val)
            
            if target < node.val and node.left:
                queue.append(node.left)
            elif target > node.val and node.right:
                queue.append(node.right)
                 
        return closestValue
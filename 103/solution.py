from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        traversals = []
        level = 0
        
        while queue:
            curr_len = len(queue)
            traversal = []
            
            '''for _ in range(curr_len):
                node = queue.popleft()
                traversal.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level % 2 == 1:
                traversal.reverse()'''
            
            # improvement:
            # improve efficiency by removing need for extra O(k) operations
            for _ in range(curr_len):
                if level % 2 == 0:
                    node = queue.popleft()
                    traversal.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                elif level % 2 == 1:
                    # reverse our operations to construct the next traversal
                    node = queue.pop()
                    traversal.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                
            traversals.append(traversal)
            level += 1
            
        return traversals
                
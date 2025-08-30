# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        solutions = []
        q = deque()
        q.append((root, 0, []))

        while len(q):
            node, total, path = q.popleft()

            # remove - need to consider negative values too
            '''if total + node.val > targetSum:
                continue'''

            # desc. mentions ROOT TO LEAF, only consider sum if we're at a leaf
            '''if total + node.val == targetSum:'''
            if not node.left and not node.right and total + node.val == targetSum:
                path.append(node.val)
                solutions.append(path)
                continue

            # we don't want to do `path.append(node.val)`
            # this modifies path as a reference for some reason???
            '''path.append(node.val)
            if node.left:
                q.append((node.left, total + node.val, path))
            if node.right:
                q.append((node.right, total + node.val, path))'''
            
            if node.left:
                q.append((node.left, total + node.val, path + [node.val]))
            if node.right:
                q.append((node.right, total + node.val, path + [node.val]))

        return solutions
        

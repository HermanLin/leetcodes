from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], minVal: int, maxVal: int) -> int:
            if not node:
               return abs(maxVal - minVal)
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            # if not node.left and not node.right:
            #     return abs(maxVal - minVal)
            
            left = dfs(node.left, minVal, maxVal)
            right = dfs(node.right, minVal, maxVal)

            return max(left, right)

        return dfs(root, root.val, root.val) 

sol = Solution() 

'''
1 1 1 => max(0, 3) => 3
    N 1 1 => 0
    2 1 1 => max(1, 3) => 3
        N 1 2 => 1
        0 1 2 => max(3, 2) => 3
            3 0 2 => max(3,3) => 3
                N 0 3 => 3
                N 0 3 => 3
            N 0 2 => 2
        
8  8  8 -> max(7,6) => 7
    3  8  8 -> max(7,5) => 7
        1  3  8 => 7
        6  3  8 -> max(5,5) => 5
            4  3  8 => 5
            7  3  8 => 5
    10 8  8 -> max(2,6) => 6
        N  8 10 => 2
        14 8 10 -> max(6,6) => 6
            13 8 14 => 6
            N  8 14 => 6

'''
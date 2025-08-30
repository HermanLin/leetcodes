# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''def doubleBFS(node):
            l_queue = deque()
            r_queue = deque()

            l_queue.append(node.left)
            r_queue.append(node.right)

            while len(l_queue) and len(r_queue):
                a = l_queue.popleft()
                b = r_queue.popleft()

                if a.val != b.val:
                    return False

                a_left = True if a.left else False
                a_right = True if a.right else False
                b_left = True if b.left else False
                b_right = True if b.right else False
                if (a_right ^ b_left) or (a_left ^ b_right):
                    # if either mirrored part is not available...
                    return False
                
                if a.right:
                    l_queue.append(a.right)
                if a.left:
                    l_queue.append(a.left)

                if b.left:
                    r_queue.append(b.left)
                if b.right:
                    r_queue.append(b.right)

            return True
                
        if not root.left and not root.right:
            return True

        if not root.left or not root.right:
            return False

        return doubleBFS(root)'''

        # DFS solution
        def doubleDFS(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False

            if left and right and left.val != right.val:
                return False

            return doubleDFS(left.right, right.left) and doubleDFS(left.left, right.right)
            
        return doubleDFS(root.left, root.right)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = right = head
        tracker = None

        while right and right.next:
            right = right.next

            if left.val == right.val: # type: ignore
                while right and left.val == right.val: # type: ignore
                    right = right.next

                if tracker:
                    # remove duplicates, right is at a new value
                    tracker.next = right
                else:
                    # tracker still at the start, relocate head
                    head = right

                # move left to the new value
                left = right
            else:
                tracker = left      # maintain tracker at node before left
                left = left.next # type: ignore

        return head
        

sol = Solution() 

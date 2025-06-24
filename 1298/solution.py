from typing import List
from collections import deque

class Solution:
    '''
        status          = [1,     0,   1,   0]
        candies         = [7,     5,   4,   100]
        keys            = [[],    [],  [1], []]
        containedBoxes  = [[1,2], [3], [],  []]
        initialBoxes    = [0]

        7 + 4 + 5 = 16 candies
    '''
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Solution below does not work. We may lose track of a box/key pair in `remaining`
        '''
        maxCandies = 0
        boxQueue = initialBoxes[:]
        remaining = set()

        # while we have boxes to check
        while len(boxQueue) > 0:
            boxToCheck = boxQueue.pop()

            # if the box is closed, we cannot progress further
            if status[boxToCheck] == 0:
                remaining.add(boxToCheck) # check if we get the key later
                continue
            
            # take the candies out
            maxCandies += candies[boxToCheck]

            # check for keys and "unlock" their boxes
            for key in keys[boxToCheck]:
                status[key] = 1

            # add boxes to the queue
            for box in containedBoxes[boxToCheck]:
                boxQueue.append(box)

        for box in remaining:
            if status[box] == 1:
                maxCandies += candies[box]

        return maxCandies
        '''

        '''
        total = 0
        queue = deque()
        pocket = set()
        visited = set()

        for box in initialBoxes:
            queue.append(box)

        while len(queue) > 0:
            box = queue.popleft()

            if status[box] == 1 and box not in visited:
                visited.add(box)
                total += candies[box]
            elif status[box] == 0:
                pocket.add(box)
                continue

            for contained in containedBoxes[box]:
                if contained not in visited:
                    queue.append(contained)

            for key in keys[box]:
                status[key] = 1

        for box in pocket:
            if status[box] == 1 and box not in visited:
                total += candies[box]

        return total
        '''

        N = len(status)
        owned = [False] * N
        opened = [False] * N
    
        # keep track of opened boxes in a new data structure
        for i in range(N):
            opened[i] = (status[i] == 1)
        
        # tag initial boxes as those we now own
        # allows us to open boxes that we gain keys for later
        for box in initialBoxes:
            owned[box] = True

        # use a queue for boxes we will own and open
        queue = deque()
        # avoid adding boxes we will process already in the queue
        added = [False] * N

        for i in range(N):
            if owned[i] and opened[i]:
                queue.append(i)
                added[i] = True

        total = 0
        while len(queue) > 0:
            box = queue.popleft()
            total += candies[box]

            for key in keys[box]:
                # for each key, open its box
                opened[key] = True
                # check if we own it and if it's not being processed yet
                if owned[key] and not added[key]:
                    queue.append(key)
                    added[key] = True
            
            for contained in containedBoxes[box]:
                # for each box contained, "own" it
                owned[contained] = True
                # check if it was "opened" and if it's not being processed yet
                if opened[contained] and not added[contained]:
                    queue.append(contained)
                    added[contained] = True
        
        return total
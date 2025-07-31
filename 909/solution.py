from collections import deque
from typing import List, Tuple


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
        n = len(board)

        def translateSquare(i) -> Tuple[int, int]:
            row = n - 1 - ((i - 1) // n)
            if (n - 1 - row) % 2:
                col = n - 1 - ((i - 1) % n)
            else:
                col = (i - 1) % n
            
            return (row, col)
        
        # starting from the first square with 0 moves
        visited = {1}
        queue = deque([(1, 0)])

        # perform BFS on each possible die roll
        while queue:
            square, moves = queue.popleft()
            x, y = translateSquare(square)
            
            # print("at square:",square,"(",x,y,") in", moves, " moves")
            
            if square == (n ** 2):
                return moves
            
            for roll in range(1, 7):
                nextSquare = min(square + roll, n**2)
                nx, ny = translateSquare(nextSquare)
                snakeOrLadder = board[nx][ny]
                
                # print("nextSquare:",nextSquare + 1,", snakeOrLadder:",snakeOrLadder)

                if snakeOrLadder == -1:
                    if nextSquare not in visited:
                        visited.add(nextSquare)
                        queue.append((nextSquare, moves + 1))
                else:
                    if snakeOrLadder not in visited:
                        visited.add(snakeOrLadder)
                        queue.append((snakeOrLadder, moves + 1))

        return -1  '''

        # improved solution, reduce complexity by forgoing the coordinate translation
        # simply flatten the board into a 1D array of n^2 size and index through
        n = len(board)
        
        # pre-process the board into a flattened 1D array
        flattened = []
        reverse = True
        for row in board:
            reverse = not reverse
            if reverse:
                flattened.extend(row.reverse())
            else:
                flattened.extend(row)

        visited = {0}
        queue = deque([(0, 0)])

        while queue:
            square, moves = queue.popleft()

            if square == (n * n) - 1:
                return moves
            
            for roll in range(1, 7):
                nextSquare = square + roll

                if nextSquare >= (n * n):
                    continue

                snakeOrLadder = flattened[nextSquare]

                if snakeOrLadder != -1:
                    nextSquare = snakeOrLadder - 1

                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append((nextSquare, moves + 1))

        return -1


            

sol = Solution() 

from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # construct graph representation
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            
            
        # start from source and check if it can reach destination
        seen = {source}
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            neighbors = graph[node]

            for n in neighbors:
                if n not in seen:
                    seen.add(n)
                    queue.append(n)
                    
        return False

        '''
        # Union-Find Solution (not by me)
        if [source, destination] in edges or [destination, source] in edges:
            return True
        roots = list(range(n))

        def find(u):
            if u == roots[u]:
                return u
            roots[u] = find(roots[u])
            return roots[u]
        
        for u, v in edges:
            roots[find(u)] = find(v)
        return find(source) == find(destination)
        '''

sol = Solution() 
print(sol.validPath(2, [[0,1],[1,2],[2,0]], 0, 2))
print(sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print(sol.validPath(1, [], 0, 0))
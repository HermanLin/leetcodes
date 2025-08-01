from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''def mutate(gene: str) -> List[str]:
            mutations = []
            for i in range(8):
                g = gene[i]
                for mg in [p for p in "ACGT" if p != g]:
                    mutations.append(gene[:i] + mg + gene[i+1:])
            return mutations
                
        valid = set(bank)
        
        if endGene not in valid:
            return -1
        
        derived = {startGene}
        queue = deque([(startGene, 0)])
        
        while queue:
            gene, count = queue.popleft()
            
            if gene == endGene:
                return count
            
            for mg in mutate(gene):
                if mg in valid and mg not in derived:
                    derived.add(mg)
                    queue.append((mg, count + 1))
                    
        return -1'''

        # improved solution
        # mutations in derived will not be queued, reduce complexity
        valid = set(bank)

        if endGene not in valid:
            return -1
        
        derived = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, count = queue.popleft()

            if gene == endGene:
                return count
            
            for protein in "ACGT":
                for i in range(8):
                    mutation = gene[:i] + protein + gene[i+1:]
                    if mutation in valid and mutation not in derived:
                        derived.add(mutation)
                        queue.append((mutation, count + 1))

        return -1

sol = Solution() 

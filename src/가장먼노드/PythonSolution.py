from math import inf
from dataclasses import dataclass
import heapq


@dataclass
class Node:
    path: int
    near: list
    
    def __lt__(self, other):
        return self.path < other.path
    
    def __gt__(self, other):
        return self.path > other.path
en

def solution(n, edges):
    nods = dict()
    
    for i in range(1, n+1):
        nods[i] = Node(inf, [])
    nods[1].path = 0
    
    for v1, v2 in edges:
        nods[v1].near.append(nods[v2])
        nods[v2].near.append(nods[v1])
    
    q = []
    heapq.heappush(q, nods[1])
    
    while q:
        curr = heapq.heappop(q)
        for node in curr.near:
            if node.path > curr.path + 1:
                node.path = curr.path + 1
                heapq.heappush(q, node)
    
    paths = tuple(map(lambda x: x.path, nods.values()))
    
    return len([i for i in paths if i == max(paths)])
        
        

if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
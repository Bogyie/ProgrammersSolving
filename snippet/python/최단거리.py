from math import inf
from collections import defaultdict


# 플로이드 와샬 -> 모든 정점에 대해 최단거리
def solution(n, vertex):
    node = [[inf for _ in range(n)] for _ in range(n)]
    result = defaultdict(int)
    
    for i, j in vertex:
        node[i-1][j-1] = 1
        
    for m in range(n):
        for s in range(n):
            for e in range(n):
                if node[s][e] > node[s][m] + node[m][e]:
                    node[s][e] = node[s][m] + node[m][e]
    
    for row in node:
        for val in row:
            if val != inf:
                result[val] += 1         
    
    print(result)
    
    return result[max(result.keys())]


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
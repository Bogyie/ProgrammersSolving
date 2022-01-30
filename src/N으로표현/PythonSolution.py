from typing import *
from functools import lru_cache
from collections import defaultdict


@lru_cache
def calc(prev:int, N:int):
    if N == 0:
        return prev - N, prev + N, prev * N
    return prev - N, prev + N, prev * N, prev // N


def solution(N:int, number:int):
    dup = lambda x, y: int(str(x)*y)
    
    result = defaultdict(set)

    for i in range(1, 8):
        result[i].add(dup(N, i))
        for val in result[i]:
            result[i + 1].update(calc(val, N))
    result[8].add(dup(N, 8))
    
    for i in range(1, 8):
        for j in range(1, 9-i):
            for a in result[i]:
                for b in result[j]:
                    result[i + j].update(calc(a, b))
            
    
    for key, val in result.items():
        if number in val:
            return key
    
    return -1
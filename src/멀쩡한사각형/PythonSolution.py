import math


def solution(w: int, h: int) -> int:
    return w * h - w - h + math.gcd(w, h)

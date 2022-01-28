from collections import defaultdict
from itertools import product
from typing import Generator, Tuple, Sequence


def make_sign_masks(length: int) -> product:
    return product((1, -1), repeat=length)


def sign_masked_numbers(numbers: Sequence[int], sign_mask: Sequence[int]) -> map:
    return map(lambda x, y: x * y, numbers, sign_mask)


def masked_numbers(numbers: Sequence[int]) -> Generator[Tuple[int], None, None]:
    for sign_mask in make_sign_masks(len(numbers)):
        yield sign_masked_numbers(numbers, sign_mask)


def solution(numbers, target):
    result_count = defaultdict(int)

    for result in masked_numbers(numbers):
        result_count[sum(result)] += 1

    return result_count[target]

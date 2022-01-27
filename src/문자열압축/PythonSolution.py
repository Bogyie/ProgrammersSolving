from typing import List
from dataclasses import dataclass


@dataclass
class StackCountString:
    string: str
    count: int

    def __str__(self) -> str:
        if self.count == 1:
            return self.string

        return str(self.count) + self.string


class CompressedString:
    def __init__(self) -> None:
        self.data: List[StackCountString] = []

    def __str__(self) -> str:
        return "".join(map(str, self.data))

    def __len__(self) -> int:
        return len(self.__str__())

    def __iadd__(self, other: str):
        if not self.data or self.data[-1].string != other:
            self.data.append(StackCountString(string=other, count=1))
        else:
            self.data[-1].count += 1
        return self


def string_split(string: str, length: int) -> str:
    end_index: int = length
    while string:
        if len(string) <= end_index:
            yield string
            string = ""
        else:
            yield string[:end_index]
            string = string[end_index:]


def solution(s):
    compress_strings: List[CompressedString] = []

    for length in range(1, len(s) + 1):
        compress_strings.append(CompressedString())
        for string in string_split(s, length):
            compress_strings[-1] += string

    return min(map(len, compress_strings))

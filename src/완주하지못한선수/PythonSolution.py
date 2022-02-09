from collections import defaultdict


def solution(participant, completion):
    players = defaultdict(int)

    for start in participant:
        players[start] += 1

    for finish in completion:
        players[finish] -= 1

    return (name for name, count in players.items() if count != 0)[0]
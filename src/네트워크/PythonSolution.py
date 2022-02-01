def solution(n, computers):
    answer = 0
    network = []
    # get_next = lambda x: [idx for idx, val in enumerate(computers[x]) if val]
    
    def get_next(index):
        computers[index][index] = 0
        result = []
        for idx, val in enumerate(computers[index]):
            if val:
                result.append(idx)
                computers[index][idx] = 0
        return result
    
    for i in range(n):
        if computers[i][i]:
            answer += 1
            network.extend(get_next(i))
        while network:
            curr = network.pop()
            network.extend(get_next(curr))
    
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
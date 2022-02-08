def solution(progresses, speeds):
    answer = []
    p = progresses[::-1]
    s = speeds[::-1]
    while p:
        p = [i + j for i, j in zip(p, s)]
        cnt = 0
        while p:
            if p[-1] >= 100:
                p.pop()
                s.pop()
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer
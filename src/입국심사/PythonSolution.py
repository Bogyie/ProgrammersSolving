# import heapq


# def officer(est_end_time, curr_end_time, delay) -> tuple:
#     return est_end_time+delay, curr_end_time+delay, delay


# def solution(n:int, times:list):
#     immigrations = []
#     heapq.heapify
#     for t in times:
#         heapq.heappush(immigrations, (t, 0, t))
    
#     for _ in range(n):
#         fastest_immigration = heapq.heappop(immigrations)
#         heapq.heappush(immigrations, officer(*fastest_immigration))
    
#     return max(map(lambda x: x[1], immigrations))


# print(solution(6, [7, 10]))


def done(n, avg_time, times) -> int:
    # -1(less), 0(equal), 1(enough)
    count = 0
    for t in times:
        count += avg_time//t 
    if n < count:
        return 1
    if n > count:
        return -1
    return 0


def solution(n:int, times:list):
    min_time = 0
    max_time = max(times) * n
    set_avg_time = lambda : (min_time + max_time) // 2
    
    avg_time = set_avg_time()
    find = done(n, avg_time, times)

    while min_time < avg_time:
        if find < 0:
            min_time = avg_time
        else:
            max_time = avg_time

        avg_time = set_avg_time()
        find = done(n, avg_time, times)
        
    return max_time


print(solution(6, [7,10]))
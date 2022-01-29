from typing import List, Tuple
from datetime import datetime
from datetime import timedelta
import heapq


def time_wrap(line:str) -> Tuple[datetime, datetime]:
    delta1 = timedelta(milliseconds=999)
    delta = timedelta(milliseconds=
              float(line[24:-1]) * 1000)
    end = datetime.fromisoformat(line[:23])
    return end-delta, end+delta1



def solution(lines:List[str]):
    perior_list = []
    pid = 0
    for ps_start, ps_end in map(time_wrap, lines):
        pid += 1
        heapq.heappush(perior_list, (ps_start.timestamp(), pid, "start"))
        heapq.heappush(perior_list, (ps_end.timestamp(), pid, "end"))
    
    processing = set()
    answer = 0
    
    def action(curr):
        if curr[2] == "start":
            processing.add(curr[1])
        else:
            processing.remove(curr[1])
    
    while perior_list:
        curr = heapq.heappop(perior_list)
        action(curr)
            
        while perior_list and curr[0] == perior_list[0][0]:
            curr = heapq.heappop(perior_list)
            action(curr)
        
        answer =  answer if answer > len(processing) else len(processing)
    
    return answer
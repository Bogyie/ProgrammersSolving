from collections import deque
from copy import deepcopy


class Array2D:
    def __init__(self, data=deque(deque())) -> None:
        self.data = data
        self.row_len = len(data)
        self.col_len = len(data[0])
    
    def __str__(self):
        return "\n".join(map(lambda x: " ".join(map(str, x)), self.data))
    
    def rotate(self, left=True):
        temp = [[None for _ in range(self.row_len)]
                for _ in range(self.col_len)]
        
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                if left:
                    temp[-1-j][i] = val
                else:
                    temp[j][-1-i] = val

        return Array2D(deque(map(deque, temp)))
    
    def sub_array(self, right=0, left=0, top=0, bottom=0, fill=None):
        """
        left < 0 : column triming left edge
        left > 0 : column padding left edge
        
        rignt < 0 : column triming right edge
        rignt > 0 : column padding right edge
        
        top < 0 : row triming top edge
        top > 0 : row padding top edge
        
        bottom < 0 : row trimng bottom edge
        bottom > 0 : row padding bottom edge
        """
        result = deepcopy(self.data)
        
        for _ in range(abs(top)):
            if top < 0:
                result.popleft()
            else:
                result.appendleft(deque((fill for _ in range(self.col_len))))
        
        for _ in range(abs(bottom)):
            if bottom < 0:
                result.pop()
            else:
                result.append(deque((fill for _ in range(self.col_len))))
                
        for row in result:
            for _ in range(abs(left)):
                if left < 0:
                    row.popleft()
                else:
                    row.appendleft(fill)
            
            for _ in range(abs(right)):
                if right < 0:
                    row.pop()
                else:
                    row.append(fill)
                    
        return Array2D(result)
    
    def move(self, right=0, top=0, fill=None):
        return self.sub_array(right=right, left=-right,
                                  top=top, bottom=-top, fill=fill)
    
    def calc(self, other, func=sum):
        result = deque()
        for self_row, other_row in zip(self.data, other.data):
            result.append(deque())
            for self_val, other_val in zip(self_row, other_row):
                result[-1].append(func(self_val, other_val))
        return Array2D(result)


def solution(key, lock) -> bool:
    key = Array2D(deque(map(deque, key)))
    lock = Array2D(deque(map(deque, lock)))
    
    k_r = key.row_len
    k_c = key.col_len
    l_r = lock.row_len
    l_c = lock.col_len
    
    def unlock(data) -> bool:
        for row in data:
            for val in row:
                if val != 1:
                    return False
        return True
    
    keys = [key]
    for _ in range(3):
        keys.append(keys[-1].rotate())
        
    for i in keys:
        i = i.sub_array(right=l_c - k_c, bottom=l_r - k_r, fill=2)
        for top in range(-l_r + 1, l_r): # -2 ~ 2
            for right in range(-l_c + 1, l_c):
                temp = i.move(right, top, fill=0)
                if unlock(temp.calc(lock, lambda x, y: x + y)):
                    return True
    return False


if __name__ == "__main__":
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
             [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
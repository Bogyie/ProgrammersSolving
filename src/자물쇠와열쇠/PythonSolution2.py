from collections import deque


class Array2D:
    def __init__(self, data=[[]]) -> None:
        self.data = data
        self.row_len = len(data)
        self.col_len = len(data[0])
    
    def __set_len(self, row_len:int, col_len:int) -> None:
        self.row_len, self.col_len = row_len, col_len

    def __to_deque(self):
        return deque(map(deque, self.data))
   
    def rotate(self, left=True) -> None:
        temp = [[None for _ in range(self.row_len)]
                for _ in range(self.col_len)]
        
        for i in range(self.row_len):  # original row
            for j in range(self.col_len):  # original col
                if left:
                    temp[-1-j][i] = self.data[i][j]
                else:
                    temp[j][-1-i] = self.data[i][j]
        
        self.data = temp
        self.__set_len(self.col_len, self.row_len)
    
    def sub_array(self, left=0, right=0, top=0, bottom=0, fill=None):
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
        result = self.__to_deque()
        
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
                    
        return Array2D(list(map(list, result)))
        
        
if __name__ == "__main__":
    x = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    y = deque(map(deque, x))
    print(y)
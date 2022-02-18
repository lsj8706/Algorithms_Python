# 섬나라 아일랜드 (BFS)
import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")

def BFS():
    global cnt
    Q = deque()
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = 0
                Q.append((i, j))
                cnt += 1
                while Q:
                    tmp = Q.popleft()
                    for k in range(8):
                        x = tmp[0]+dx[k]
                        y = tmp[1]+dy[k]
                        if 0<=x<n and 0<=y<n and board[x][y] == 1:
                            board[x][y] = 0
                            Q.append((x,y))
            else:
                pass


if __name__ == "__main__":
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    dx=[-1, -1, -1, 0, 1, 0, 1, 1]
    dy=[1, -1, 0, 1, 0, -1, 1, -1]

    cnt = 0
    BFS()
    print(cnt)

   
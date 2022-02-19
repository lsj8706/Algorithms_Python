# 토마토 (BFS)
import sys
from collections import deque
#sys.stdin = open("in4.txt", "rt")

def BFS():
    while Q:
        tmp = Q.popleft()
        for k in range(4):
            xx = tmp[0]+dx[k]
            yy = tmp[1]+dy[k]
            if 0<=xx<n and 0<=yy<m and board[xx][yy]==0:
                board[xx][yy] = 1
                dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
                s.add(dis[xx][yy])
                Q.append((xx, yy))

if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    dis = [[0 for _ in range(m)] for _ in range(n)]
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]

    Q = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                Q.append((i, j))
    
    s = set()
    BFS()

    for x in board:
        if 0 in x:
            print(-1)
            sys.exit()

    print(max(s))
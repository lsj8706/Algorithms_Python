# 안전영역 (BFS)
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

def BFS(L):
    global res
    cnt = 0
    Q = deque()
    ch = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] <= L:
                ch[i][j] = 1

    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                ch[i][j] = 1
                Q.append((i,j))
                cnt += 1
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        x = tmp[0]+dx[k]
                        y = tmp[1]+dy[k]
                        if 0<=x<n and 0<=y<n and ch[x][y] == 0:
                            ch[x][y] = 1
                            Q.append((x,y))
    if cnt > res:
        res = cnt

if __name__ == "__main__":
    n = int(input())
    board = []
    max = -2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] > max:
                max = tmp[j]
        board.append(tmp)
    
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]

    res = 0
    for i in range(1, max):
        BFS(i)
    
    print(res)
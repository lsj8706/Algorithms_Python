# 단지 번호 붙이기 (DFS, BFS)
import sys
from collections import deque
#sys.stdin = open("in5.txt", "rt")

def BFS(blankX, blankY):
    Q = deque()
    Q.append((blankX, blankY))
    isOne = False
    while Q:
        tmp = Q.popleft()
        for j in range(5):
            x = tmp[0]+dx[j] # x좌표
            y = tmp[1]+dy[j] # y좌표
            if 0<=x<n and 0<=y<n:
                if board[x][y] == 1 and ch[x][y] == 0:
                    isOne = True
                    ch[x][y] = 1
                    res[x][y] = L
                    cnt[L-1] += 1
                    Q.append((x,y))
                if board[x][y] == 0 and ch[x][y] == 0:
                    ch[x][y] = 1
                    res[x][y] = 0

    return isOne

if __name__ == "__main__":
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input())))
    res = [[-1 for _ in range(n)] for _ in range(n)]

    # 상하좌우 좌표
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    ch = [[0 for _ in range(n)] for _ in range(n)]

    L = 1
    isdone = False
    cnt = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                res[i][j] = 0
            else:
                if res[i][j] == -1:
                    cnt.append(0)
                    isOne = BFS(i,j)
                    if isOne:
                        L += 1


    print(L-1)
    cnt.sort()
    for x in cnt:
        print(x)
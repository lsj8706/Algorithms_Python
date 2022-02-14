# 사과나무 (BFS)
import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")

def BFS():
    L = 0
    total = farm[n//2][n//2]

    while True:
        if L == n//2:
            break
        size = len(Q)
        for i in range(size):
            tmp = Q.popleft()
            for j in range(4):
                x = tmp[0]+dx[j] # x좌표
                y = tmp[1]+dy[j] # y좌표
                if ch[x][y] == 0:
                    total += farm[x][y]
                    ch[x][y] = 1
                    Q.append((x,y))
        L += 1
    print(total)

if __name__ == "__main__":
    n = int(input())
    farm = []
    for _ in range(n):
        row = list(map(int, input().split()))
        farm.append(row)
    
    # 시계방향 좌표
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ch = [[0 for _ in range(n)] for _ in range(n)]
    Q = deque()
    Q.append((n//2, n//2)) # 중앙부터 시작
    ch[n//2][n//2] = 1
    BFS()

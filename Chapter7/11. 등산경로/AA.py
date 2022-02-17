# 등산경로 (DFS)
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(x, y):
    global cnt
    if x == maxX and y == maxY:
        cnt += 1
    else:
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0<=nextX<n and 0<=nextY<n:
                if board[nextX][nextY]>board[x][y] and ch[nextX][nextY]==0:
                    ch[nextX][nextY] = 1
                    DFS(nextX, nextY)
                    ch[nextX][nextY] = 0


if __name__ == "__main__":
    n = int(input())
    board = []
    max = -2147000000
    min = 2147000000
    # 최솟값과 최댓값의 위치 찾고 리스트에 넣기
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                minX = i
                minY = j
            if tmp[j] > max:
                max = tmp[j]
                maxX = i
                maxY = j
        board.append(tmp)

    ch = [[0 for _ in range(n)] for _ in range(n)]
    ch[minX][minY] = 1
    
    # 상하좌우 좌표
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    DFS(minX, minY)
    print(cnt)
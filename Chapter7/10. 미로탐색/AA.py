# 미로탐색(DFS)
import sys
sys.stdin = open("input.txt", "rt")

def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0<=nextX<=6 and 0<=nextY<=6 and maze[nextX][nextY] == 0:
                maze[nextX][nextY] = 1
                DFS(nextX, nextY)
                maze[nextX][nextY] = 0


if __name__ == "__main__":
    maze  = []
    for _ in range(7):
        maze.append(list(map(int, input().split())))
    maze[0][0] = 1

    # 상하좌우 좌표
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    DFS(0,0)
    print(cnt)
# 미로의 최단거리 통로 (BFS)
import sys
from collections import deque
#sys.stdin = open("in3.txt" ,"rt")

def BFS():
    Q = deque()
    Q.append((0,0))
    while Q:
        tmp = Q.popleft()
        if tmp == (6, 6):
            print(dis[6][6])
            break
        else:
            for j in range(4):
                x = tmp[0]+dx[j] # x좌표
                y = tmp[1]+dy[j] # y좌표
                if 0<=x<=6 and 0<=y<=6:
                    if maze[x][y] == 0 and ch[x][y] == 0:
                        ch[x][y] = 1
                        dis[x][y] = dis[tmp[0]][tmp[1]] + 1
                        Q.append((x,y))
    else:
        print(-1)




if __name__ == "__main__":
    maze = []
    for _ in range(7):
        maze.append(list(map(int, input().split())))
    
    # 상하좌우 좌표
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    ch = [[0 for _ in range(7)] for _ in range(7)]
    dis = [[0 for _ in range(7)] for _ in range(7)]
    ch[0][0] = 1
    dis[0][0] = 0
    BFS()

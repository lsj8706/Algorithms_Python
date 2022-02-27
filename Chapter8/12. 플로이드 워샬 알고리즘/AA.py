# 플로이드 워샬 알고리즘
import sys
#sys.stdin = open("in5.txt", "rt")

if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000 for _ in range(n+1)] for _ in range(n+1)]
    
    # 출발지와 목적지가 같은 경우는 0으로 초기화
    for i in range(1, n+1):
        dis[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c
    
    # 플로이드 워샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print('M', end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
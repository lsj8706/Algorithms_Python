# 회장뽑기(플로이드-워샬 응용)
import sys
#sys.stdin = open("in5.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    dis = [[5000 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        dis[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1
    
    # 플로이드 워샬 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    
    res = []

    for x in range(1, n+1):
        res.append(max(dis[x][1:]))

    minRes = min(res)
    print(minRes, res.count(minRes))
    for i in range(len(res)):
        if res[i] == minRes:
            print(i+1, end=' ')
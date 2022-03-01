# 위상정렬(그래프 정렬)
import sys
sys.stdin = open("input.txt", "rt")

def adjacentVertex(v):
    l = []
    for i in range(n+1):
        if dis[v][i] == 1:
            l.append(i)
    return l

def DFS(v):
    visited[v] = 1
    adjacent = adjacentVertex(v)
    for x in adjacent:
        if visited[x] == 0:
            DFS(x)
    res.insert(0, v)

if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        dis[a][b] = 1
    
    visited = [0]*(n+1)
    res = []

    for i in range(1, n+1):
        if visited[i] == 0:
            DFS(i)
    
    print(res)
# 경로 탐색(그래프 DFS)
import sys
#sys.stdin = open("input.txt", "rt")

def getMatrix(s, e):
    matrix[s][e] = 1
    return

def getAdjacent(v):
    queue = []
    for i in range(1, n+1):
        if matrix[v][i] == 1:
            queue.append(i)
    return queue

def DFS(L):
    global cnt
    if L == n:
        cnt += 1
    else:
        adjacent = getAdjacent(L)
        for x in adjacent:
            if visited[x] == 0 :
                visited[x] = 1
                DFS(x)
                visited[x] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        getMatrix(s, e)
    
    cnt = 0
    visited = [0] * (n+1)
    visited[1] = 1
    DFS(1)
    print(cnt)
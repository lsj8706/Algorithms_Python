# 인접 행렬
import sys
sys.stdin = open("input.txt", "rt")

def matrix(s, e, v):
    res[s-1][e-1] = v
    return

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        s, e, v = map(int, input().split())
        matrix(s, e, v)
    
    for i in res:
        for j in i:
            print(j, end=' ')
        print()
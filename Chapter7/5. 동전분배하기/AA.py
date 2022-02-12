# 동전 분배하기 (DFS)
import sys
#sys.stdin = open("in2.txt", "rt")

def DFS(L, a, b, c):
    global res
    if L == n:
        if a == b or b == c or a == c:
            return
        else:
            diff = max(a,b,c)-min(a,b,c)
            if diff < res:
                res = diff
    else:
        DFS(L+1, a+coin[L], b, c)
        DFS(L+1, a, b+coin[L], c)
        DFS(L+1, a, b, c+coin[L])


if __name__ == "__main__":
    n = int(input())
    coin = []
    for _ in range(n):
        coin.append(int(input()))
    res = 2147000000
    DFS(0, 0, 0, 0)
    print(res)
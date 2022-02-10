# 휴가 (DFS 활용)
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(L, priceSum):
    global res
    if L > n:
        return
    if L == n:
        if priceSum > res:
            res = priceSum
    else:
        if priceSum > res:
            res = priceSum
        DFS(L+1, priceSum)
        if L+table[L][0] <= n:
            DFS(L+table[L][0], priceSum+table[L][1])


if __name__ == "__main__":
    n = int(input())
    table = []
    for _ in range(n):
       t, p = map(int, input().split())
       table.append((t, p))
    
    res = 0
    DFS(0, 0)
    print(res)
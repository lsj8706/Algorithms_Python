# 동전 바꿔주기(DFS)
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(coin[L][1]+1):
            DFS(L+1, sum+(i*coin[L][0]))


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    coin = []
    for _ in range(k):
        p, n = map(int, input().split())
        coin.append((p, n))

    cnt = 0
    DFS(0, 0)
    print(cnt)
# 동전 교환
import sys
#sys.stdin = open("in2.txt", "rt")

def DFS(money, L):
    global res
    if money < 0:
        return
    if L >= res:
        return
    if money == 0:
        if L < res:
            res = L
        return
    else:
        for x in coin:
            DFS(money-x, L+1)


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    money = int(input())
    res = 2147000000
    DFS(money, 0)
    print(res)

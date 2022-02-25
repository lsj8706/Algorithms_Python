# 동전 교환 (냅색 알고리즘)
import sys
#sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())
    dy = [2147000000]*(money+1) # dy[j]는 j원을 거슬러 주는데 사용된 동전의 최소 개수
    dy[0] = 0
    for i in range(n):
        for j in range(coin[i], money+1):
            dy[j] = min(dy[j], dy[j-coin[i]]+1)
    print(dy[money])
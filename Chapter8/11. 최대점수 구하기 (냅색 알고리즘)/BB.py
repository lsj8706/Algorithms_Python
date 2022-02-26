# 최대점수 구하기(냅색 알고리즘) with 1차원 배열
import sys
sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0 for _ in range(m+1)]
    # dy[j]는 j시간이 주어졌을 때 최대 점수
    for i in range(0, n):
        score, time = map(int, input().split())
        for j in range(m, time-1, -1):
            dy[j] = max(dy[j], dy[j-time]+score)

    print(dy[m])
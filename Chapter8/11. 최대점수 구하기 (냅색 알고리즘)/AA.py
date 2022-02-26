# 최대점수 구하기(냅색 알고리즘) with 2차원 배열
import sys
#sys.stdin = open("input.txt", "rt")

if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # dy[i][j]는 i번째 문제까지 고려하고 j시간이 주어졌을 때 최대 점수
    for i in range(1, n+1):
        score, time = map(int, input().split())
        for j in range(time, m+1):
            dy[i][j] = max(dy[i-1][j], dy[i-1][j-time]+score)

    print(dy[n][m])
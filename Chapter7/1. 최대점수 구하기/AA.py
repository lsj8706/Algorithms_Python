# 최대점수 구하기(DFS)
from os import times
import sys
#sys.stdin = open("input.txt", "rt")


def DFS(L, scoreSum, timeSum):
    global res
    if timeSum > m:
        return
    if L == n:
        if scoreSum > res:
            res = scoreSum
    else:
        DFS(L+1, scoreSum, timeSum)
        DFS(L+1, scoreSum+problems[L][0], timeSum+problems[L][1])

if __name__ == "__main__":
    n, m = map(int, input().split())
    problems = []
    for _ in range(n):
        score, time = map(int, input().split())
        problems.append((score, time))

    res = 0
    DFS(0, 0, 0)
    print(res)
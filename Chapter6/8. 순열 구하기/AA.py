# 순열 구하기
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if i not in res:
                res[L] = i
                DFS(L+1)
                res[L] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
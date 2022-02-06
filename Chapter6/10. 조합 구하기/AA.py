# 조합 구하기
import sys
#sys.stdin = open("in3.txt" ,"rt")

def DFS(L):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
    else:
        if L==0:
            for i in range(1, n+1):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    DFS(L+1)
                    ch[i] = 0
        else:
            for i in range(res[L-1]+1, n+1):
                if ch[i] == 0:
                    ch[i] = 1
                    res[L] = i
                    DFS(L+1)
                    ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)
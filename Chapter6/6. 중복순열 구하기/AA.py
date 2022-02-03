# 중복순열 구하기
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(index):
    global cnt
    if index == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1,n+1):
            res[index] = i
            DFS(index+1)

    
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)

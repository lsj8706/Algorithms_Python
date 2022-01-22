# 역수열 (그리디)
import sys
#sys.stdin = open("in1.txt", "rt")
n = int(input())
l = list(map(int, input().split()))

res = [0] * n

for i in range(1, n+1):
    frontBigNum = l[i-1] # i 앞에 있는 i 보다 큰 수 의 개수
    cnt = 0
    for j in range(n):
        if cnt == frontBigNum:
            if res[j] == 0:
                res[j] = i
                break
            else:
                continue
        else:
            if res[j] == 0 or res[j] > i:
                cnt += 1
            
for x in res:
    print(x, end=' ')
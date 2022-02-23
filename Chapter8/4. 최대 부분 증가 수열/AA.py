# 최대 부분 증가수열
import sys
#sys.stdin = open("in2.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n+1)

dy[1] = 1


for i in range(2, n+1):
    maxLen = 0
    for j in range(1, i):
        if arr[i] > arr[j]:
            if dy[j] > maxLen:
                maxLen = dy[j]
    dy[i] = maxLen+1

print(max(dy))



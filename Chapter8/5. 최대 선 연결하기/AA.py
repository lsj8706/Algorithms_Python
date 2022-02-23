# 최대 선 연결하기
import sys
#sys.stdin = open("in4.txt" ,"rt")

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0]*(n+1)

dy[1] = 1

for i in range(2, n+1):
    maxNum = 0
    for j in range(1, i):
        if arr[j] < arr[i]:
            if dy[j] > maxNum:
                maxNum = dy[j]
    dy[i] = maxNum + 1

print(max(dy))
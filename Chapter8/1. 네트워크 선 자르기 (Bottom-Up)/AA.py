# 네트워크 선 자르기 (Bottom-Up)
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
dy = [0]*(n+1)

dy[1] = 1
dy[2] = 2

for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]

print(dy[n])




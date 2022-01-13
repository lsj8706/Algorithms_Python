# 곳감(모래시계)
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    row, direction, num = map(int, input().split())
    row -= 1
    for _ in range(num):
        if direction == 0:
            farm[row] = farm[row][1:] + [farm[row][0]]
        else:
            farm[row] = [farm[row][n-1]] + farm[row][:n-1]

total = 0
s=0
e=n
for i in range(n):
    for j in range(s,e):
        total += farm[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(total)


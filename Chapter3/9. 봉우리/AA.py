# 봉우리
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
for x in m:
    x.append(0)
    x.insert(0,0)
m.append([0]*(n+2))
m.insert(0, [0]*(n+2))

res = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        mine = m[i][j]
        if m[i-1][j] < mine and m[i][j-1] < mine and m[i][j+1] < mine and m[i+1][j] < mine:
            res += 1
print(res)
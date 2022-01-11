# 격자판 최대합
import sys

#sys.stdin = open("input.txt", "rt")
n = int(input())
l = []
result = []
for i in range(n):
    l.append(list(map(int, input().split())))

dia = 0
dia2 = 0
for i in range(n):
    col = 0
    row = 0
    for j in range(n):
        col += l[j][i]
        row += l[i][j]
        if i+j == n-1:
            dia2 += l[i][j]
    result.append(col)
    result.append(row)
    dia += l[i][i]

result.append(dia)
result.append(dia2)

result.sort()
print(result[-1])
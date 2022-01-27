# 공주 구하기 (큐)
import sys
#sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(i+1)

cnt = 1

while len(l) != 1:
    if cnt != k:
        a = l.pop(0)
        l.append(a)
        cnt += 1
    else:
        l.pop(0)
        cnt = 1

print(l[0])
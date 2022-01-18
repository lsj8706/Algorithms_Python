# 씨름 선수 (그리디)
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
people = []
for _ in range(n):
    a, b = map(int, input().split())
    people.append((a,b))
people.sort()


cnt = 0
i = 0
while i < n:
    for j in range(i, n):
        if people[j][1] > people[i][1]:
            break
    else:
        cnt += 1
    i += 1



print(cnt)
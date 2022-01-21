# 침몰하는 타이타닉
import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort()
res = 0

while people:
    if len(people) > 1:
        if people[0] + people[-1] <= m:
            res += 1
            people.pop(0)
            people.pop()
        else:
            res += 1
            people.pop()
    else:
        res += 1
        break
print(res)
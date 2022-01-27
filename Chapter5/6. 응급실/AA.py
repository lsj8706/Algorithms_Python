# 응급실 (큐)
import sys
from collections import deque
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
patientsQ = [(index, val) for index, val in enumerate(list(map(int, input().split())))]
patientsQ = deque(patientsQ)
cnt = 0

while True:
    cur = patientsQ.popleft()
    for i, v in patientsQ:
        if v > cur[1]:
            patientsQ.append(cur)
            break
    else:
        if cur[0] != m:
            cnt += 1
        else:
            cnt += 1
            break

print(cnt)

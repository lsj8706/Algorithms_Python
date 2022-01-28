# 교육과정 설계 (큐)
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
subjects = input()
n = int(input())

for i in range(n):
    s = input()
    Q = deque(subjects)
    for x in s:
        if x in Q:
            if x == Q[0]:
                sub = Q.popleft()
            else:
                print(f"#{i+1} NO")
                break
        else:
            pass
    else:
        if len(Q) >= 1:
            print(f"#{i+1} NO")
        else:
            print(f"#{i+1} YES")


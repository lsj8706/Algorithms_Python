# 회의실 배정(그리디)
import sys
#sys.stdin = open("in1.txt", "rt")
n = int(input())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a,b))
# 튜플이 들어 있는 list를 튜플의 두번째 아이템을 기준으로 정렬하는 방법(람다 사용)
l.sort(key=lambda x : (x[1], x[0]))

et = 0
cnt = 0

for s, e in l:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
 
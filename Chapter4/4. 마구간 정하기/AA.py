# 마구간 정하기(결정 알고리즘)
import sys
#sys.stdin = open("input.txt", "rt")

def Count(distance):
    cnt = 1
    position = l[0]
    for i in range(1,n):
        if l[i]-position >= distance:
            cnt += 1
            position = l[i]
    return cnt 


n, c = map(int, input().split())
largest = 0
l = []
for _ in range(n):
    tmp = int(input())
    l.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1
print(res)
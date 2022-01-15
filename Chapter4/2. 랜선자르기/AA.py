# 랜선 자르기
import sys
#sys.stdin = open("input.txt", "rt")

def Count(len):
    cnt = 0
    for x in l:
        cnt += x//len
    return cnt

k, n = map(int, input().split())
l = []
largest = 0
for _ in range(k):
    tmp = int(input())
    l.append(tmp)
    largest = max(largest, tmp) # 가장 큰 수 찾기

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
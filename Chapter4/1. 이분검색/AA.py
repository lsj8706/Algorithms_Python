# 이분검색
import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
s = 0
e = n - 1

while s <= e:
    mid = (s+e)//2
    if l[mid] == m:
        print(mid+1)
        break
    elif l[mid] > m:
        e = mid - 1
    else:
        s = mid + 1

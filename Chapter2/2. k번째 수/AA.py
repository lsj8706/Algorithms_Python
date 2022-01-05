# k번째 수
import sys
sys.stdin = open("in1.txt", "rt")
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    numList = list(map(int, input().split()))
    numList = numList[s-1:e]
    numList.sort()
    print(f"#{t+1} {numList[k-1]}")
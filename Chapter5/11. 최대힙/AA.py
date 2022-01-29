# 최대힙
import sys
import heapq
#sys.stdin = open("input.txt", "rt")

heap = []

while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        res = -(heapq.heappop(heap))
        print(res)
    else:
        heapq.heappush(heap, -num)
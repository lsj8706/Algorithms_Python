# 창고 정리
import sys
#sys.stdin = open("input.txt", "rt")
l = int(input())
box = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    maxValue = max(box)
    maxIndex = box.index(maxValue)
    box[maxIndex] -= 1
    minValue = min(box)
    minIndex = box.index(minValue)
    box[minIndex] += 1

print(max(box) - min(box))

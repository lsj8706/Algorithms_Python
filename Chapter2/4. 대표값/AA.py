# 대표값
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
numList = list(map(int, input().split()))
avg = round(sum(numList)/n)
minGap = float('inf')
index = 0
for i, num in enumerate(numList):
    if abs(num-avg) < minGap:
        index = i
        minGap = abs(num-avg)
    elif abs(num-avg) == minGap:
        if numList[index] < num:
            index = i
print(avg, index + 1)
            
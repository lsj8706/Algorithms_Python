# 정다면체
import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i+j
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1
minF = 0
sumList = []
for sum, f in list(dic.items()):
    if f > minF:
        minF = f
        sumList.clear()
        sumList.append(sum)
    elif f == minF:
        sumList.append(sum)
sumList.sort()
for x in sumList:
    print(x, end=" ")
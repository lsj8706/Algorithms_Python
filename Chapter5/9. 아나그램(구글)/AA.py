# 아나그램(구글)
import sys
#sys.stdin = open("input.txt", "rt")
first = input()
second = input()
firstDic = {}
secondDic = {}

for x in first:
    if x in firstDic:
        firstDic[x] += 1
    else:
        firstDic[x] = 1
for x in second:
    if x in secondDic:
        secondDic[x] += 1
    else:
        secondDic[x] = 1

if firstDic == secondDic:
    print("YES")
else:
    print("NO")

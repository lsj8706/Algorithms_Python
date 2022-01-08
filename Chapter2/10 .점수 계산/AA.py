# 점수 계산
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
oneList = []
result = 0
oxList = list(map(int, input().split()))

for x in oxList:
    if x == 0:
        oneList.clear()
    else:
        oneList.append(1)
        result += len(oneList)

print(result)
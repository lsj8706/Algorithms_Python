# 두 리스트 합치기
import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
firstList = list(map(int, input().split()))
m = int(input())
secondList = list(map(int, input().split()))

result = firstList + secondList
result.sort()

for x in result:
    print(x, end=" ")

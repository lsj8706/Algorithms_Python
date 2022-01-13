# 사과나무(다이아몬드)
import sys
#sys.stdin = open("in2.txt", "rt")
n = int(input())
farm = [list(map(int,input().split())) for x in range(n)]
mid = n // 2
total = 0
i = 0

for x in range(0, n):
    if x < mid:
        total += sum(farm[x][mid-i:mid+i+1])
        i+=1
    else:
        total += sum(farm[x][mid-i:mid+i+1])
        i-=1
print(total)
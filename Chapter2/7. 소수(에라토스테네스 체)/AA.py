# 소수(에라토스테네스 체)
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
numList = [True] * n

# n의 최대 약수는 sqrt(n) 이하이다 => i = sqrt(n)까지 검사
m = int(n ** 0.5)
for i in range(2, m+1):
    if numList[i] == True:
        for j in range(i+i, n, i):
            numList[j] = False

primeList = [i for i in range(2,n) if numList[i] == True]

if (n == 2):
    print(1)
else:
    print(len(primeList))


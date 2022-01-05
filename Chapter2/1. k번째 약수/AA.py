# K번째 약수
import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())

num = 0
for i in range(1,n+1):
    if n % i == 0:
        num += 1
    if num == k:
        print(i)
        break
else:
    print(-1)
# if num > k or num < k:
#    print(-1)

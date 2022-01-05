# k번째 큰 수
import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
numList = list(map(int, input().split()))
sumList = set()
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            num = numList[i]+numList[j]+numList[l]
            sumList.add(num)
sumList = list(sumList)
sumList.sort(reverse=True)
print(sumList[k-1])



    


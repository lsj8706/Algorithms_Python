# k번째 큰 수
import sys
#sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
numList = list(map(int, input().split()))
sumList = []
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            num = numList[i]+numList[j]+numList[l]
            sumList.append(num)
sumList.sort(reverse=True)

count = 0
predNum = 0
for num in sumList:
    if predNum != num:
        count += 1
        predNum = num
    if count == k:
        print(num)
        break



    


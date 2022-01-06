# 자릿수의 합
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
numL = list(map(int, input().split()))
maxIndex = 0
maxSum = 0

def digit_sum(x):
    sum = 0
    for x in str(x):
        sum += int(x)
    return sum


for idx, num in enumerate(numL):
    sum = digit_sum(num)
    if sum > maxSum:
        maxSum = sum
        maxIndex = idx
print(numL[maxIndex])



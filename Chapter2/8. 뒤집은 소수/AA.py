# 뒤집은 소수
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
numList = list(map(int, input().split()))

def reverse(x):
    isFirst = True
    result = ""
    reverseNumList = list(str(x))
    reverseNumList.reverse()
    for i in reverseNumList:
        if isFirst and i == '0':
            pass
        elif isFirst and i != '0':
            result += i
            isFirst = False
        else:
            result += i
    return int(result)

def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    m = int(x ** 0.5)
    for i in range(2, m+1):
        if x % i == 0:
            return False
    return True

for i in numList:
    reverseNum = reverse(i)
    if isPrime(reverseNum):
        print(reverseNum, end=' ')
        
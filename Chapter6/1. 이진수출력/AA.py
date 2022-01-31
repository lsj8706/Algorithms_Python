# 이진수 출력(재귀)
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
res = []

def convertToBinary(n, res):
    if n > 1:
        remainder = n % 2
        n = n // 2
        convertToBinary(n, res)
        res.append(remainder)
        return res
    else:
        res.append(n)
        return

res = convertToBinary(n, res)
for x in res:
    print(x, end='')

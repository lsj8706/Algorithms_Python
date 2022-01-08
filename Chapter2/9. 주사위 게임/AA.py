# 주사위 게임
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
moneySum = []

for i in range(n):
    numList = list(map(int, input().split()))
    numList.sort(reverse=True)
    if numList.count(numList[0]) == 3:
        moneySum.append(10000 + numList[0]*1000)
    elif numList.count(numList[0]) == 1 and numList.count(numList[1]) == 1 and numList.count(numList[2]) == 1:
        moneySum.append(100*numList[0])
    else:
        if numList.count(numList[0]) == 2:
            moneySum.append(1000 + numList[0]*100)
        else:
            moneySum.append(1000 + numList[1]*100)

moneySum.sort(reverse=True)
print(moneySum[0])
# 증가수열 만들기 (그리디)
import sys
#sys.stdin = open("input2.txt", "rt")
n = int(input())
l = list(map(int, input().split()))

cnt = 0
res = ""
lastNum = 0
notFinished = True

while notFinished:
    if l[0] > lastNum and l[-1] > lastNum:
        if l[0] <= l[-1]:
            lastNum = l[0]
            l.pop(0)
            res += "L"
        else:
            lastNum = l[-1]
            l.pop()
            res += "R"
        cnt += 1
    elif l[0] > lastNum and l[-1] <= lastNum:
        lastNum = l[0]
        l.pop(0)
        cnt += 1
        res += "L"
    elif l[0] <= lastNum and l[-1] > lastNum:
        lastNum = l[-1]
        l.pop()
        cnt += 1
        res += "R"
    else:
        notFinished = False

print(cnt)
print(res)
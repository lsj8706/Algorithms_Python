# 쇠막대기
import sys
#sys.stdin = open("input2.txt", "rt")
word = input()
stick = []
for x in word:
    stick.append(x)

last = ""
res = 0
numberOfStick = 0
for x in stick:
    if x == '(':
        numberOfStick += 1
        last = x
    else:
        if last + x == "()":
            numberOfStick -= 1
            res += numberOfStick
            last = x
        elif last + x == "))":
            res += 1
            numberOfStick -= 1
            last = x
    
print(res)
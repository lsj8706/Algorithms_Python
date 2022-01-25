# 후위식 연산
import sys
#sys.stdin = open("input.txt", "rt")
s = input()
stack = []

for x in s:
    if x.isdecimal():
        stack.append(x)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        if x == '+':
            stack.append(b+a)
        elif x == '-':
            stack.append(b-a)
        elif x == '*':
            stack.append(b*a)
        else:
            stack.append(b//a)
print(stack.pop())

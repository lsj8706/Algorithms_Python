# 회문 문자열 검사
import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(n):
    isSame = True
    l = list(input())
    revL = list(reversed(l))
    for j in range(len(l)):
        if l[j].upper() == revL[j].upper():
            pass
        else:
            isSame = False
            break
    if isSame:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")

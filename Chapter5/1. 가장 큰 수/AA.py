# 가장 큰 수
import sys
#sys.stdin = open("input2.txt" ,"rt")
n, m = map(int, input().split())

cnt = 0
res = []
n = list(str(n))
n = list(map(int, n))

while len(n) != 0:
    a = n.pop(0)
    if len(res) == 0:
        res.append(a)
    else:
        while len(res) != 0:
            if res[-1] < a and cnt < m:
                res.pop()
                cnt += 1
            else:
                break
        res.append(a)

if cnt < m:
    for _ in range(m-cnt):
        res.pop()

for x in res:
    print(x, end='')
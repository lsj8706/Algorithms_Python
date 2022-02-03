# 바둑이 승차 (DFS)
import sys
#sys.stdin = open("in5.txt", "rt")

def DFS(index, sum, tsum):
    global res
    if sum + (total-tsum) < res:
        return
    if sum > c:
        return
    if index == n:
        if sum > res:
            res = sum
        else:
            return
    else:
        DFS(index+1, sum+l[index], tsum+l[index])
        DFS(index+1, sum, tsum+l[index])



if __name__ == "__main__":
    c, n = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(int(input()))
    res = 0
    total = sum(l)
    DFS(0, 0, 0)
    print(res)

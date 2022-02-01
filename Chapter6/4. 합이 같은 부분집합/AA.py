# 합이 같은 부분 집합 (DFS)
import sys
#sys.stdin = open("input.txt" ,"rt")

def DFS(index, l):
    if index == len(l):
        s = set()
        for i in range(len(l)):
            if ch[i] == 1:
                s.add(l[i])
        differenceSet = set(l) - s
        if sum(differenceSet) == sum(s):
            return True
        return False
    else:
        ch[index] = 1
        isSame = DFS(index+1, l)
        if isSame:
            return isSame
        ch[index] = 0
        isSame = DFS(index+1, l)
        return isSame
  
    

if __name__ == "__main__":
    n = int(input())
    ch = [0]*n
    l = list(map(int, input().split()))

    res = DFS(0, l)
    if res:
        print("YES")
    else:
        print("NO")
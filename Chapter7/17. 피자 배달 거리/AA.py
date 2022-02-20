# 피자 배달 거리 (DFS)
import sys
from itertools import combinations
#sys.stdin = open("input.txt", "rt")

def minDis(p, x, y):
    min = 2147000000
    for store in p:
        dis = abs(store[0]-x) + abs(store[1]-y)
        if dis < min:
            min = dis
    return min

if __name__ == "__main__":
    n, m = map(int, input().split())
    board =  []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    pizza = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                pizza.append((i,j))

    c = list(combinations(pizza, m))
    res = []
    for p in c:
        tot = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    tot += minDis(p, i, j)
        res.append(tot)
    
    print(min(res))
# 알리바바와 40인의 도둑(Top-Down)
import sys
#sys.stdin = open("input.txt", "rt")

def DFS(x, y, sum):
    global res
    if sum > res:
        return
    if x >= n or y >= n:
        return
    if x == n-1 and y == n-1:
        sum = sum + board[n-1][n-1]
        if sum < res:
            res = sum
    else:
        if ch[x][y] == 0 or sum+board[x][y] < ch[x][y]:
            ch[x][y] = sum+board[x][y]
            DFS(x+1, y, sum+board[x][y])
            DFS(x, y+1, sum+board[x][y])
        else:
            return


if __name__ == "__main__":
    n = int(input())
    board = []
    ch = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int, input().split())))
    res = 2147000000
    DFS(0, 0, 0)
    print(res)

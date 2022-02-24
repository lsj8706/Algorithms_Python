# 알리바바와 40인의 도둑(Bottom-Up)
import sys
#sys.stdin = open("in1.txt", "rt")

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        if 0<=i-1<n or 0<=j-1<n:
            if 0<=i-1<n and 0<=j-1<n:
                top = dy[i-1][j]
                left = dy[i][j-1]
                if top <= left:
                    dy[i][j] = top + board[i][j]
                else:
                    dy[i][j] = left + board[i][j]
            elif 0<=i-1<n:
                top = dy[i-1][j]
                dy[i][j] = top + board[i][j]
            else:
                left = dy[i][j-1]
                dy[i][j] = left + board[i][j]
        else:
            dy[i][j] = board[i][j]

print(dy[n-1][n-1])
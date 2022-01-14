# 격자판 회문수
import sys
#sys.stdin = open("input.txt", "rt")

def isCircular(l):
    revL = list(reversed(l))
    for i in range(len(l)):
        if l[i] == revL[i]:
            pass
        else:
            return False
    return True

def check(board):
    res = 0
    for i in range(7):
        if isCircular(board[i][:5]):
            res += 1
        if isCircular(board[i][1:6]):
            res += 1
        if isCircular(board[i][2:7]):
            res += 1
        for j in range(3):
            l = []
            for k in range(5):
                l.append(board[j+k][i])
            if isCircular(l):
                res += 1

    return res


board = [list(map(int, input().split())) for _ in range(7)]
print(check(board))
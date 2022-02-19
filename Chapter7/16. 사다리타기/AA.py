# 사다리 타기 (DFS)
import sys
sys.stdin = open("input.txt", "rt")

def DFS(L, x, y):
    if x == 9:
        if board[x][y] == 2:
            print(L)
            sys.exit()
    else:
        if 0<=y-1<10 and board[x][y-1] == 1:
            board[x][y] = 0
            DFS(L, x, y-1)
            board[x][y] = 1
        elif 0<=y+1<10 and board[x][y+1] == 1:
            board[x][y] = 0
            DFS(L, x, y+1)
            board[x][y] = 1
        else:
            board[x][y] = 0
            DFS(L, x+1, y)
            board[x][y] = 1

if __name__ == "__main__":
    board = []
    for _ in range(10):
        board.append(list(map(int, input().split())))

    people = [0, 2, 5, 7, 9]
    for x in people:
        DFS(x, 0, x)

  
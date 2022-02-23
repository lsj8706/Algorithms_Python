# 계단오리기 (Top-Down)
import sys
sys.stdin = open("input.txt", "rt")

def DFS(len):
    if len == 1 or len == 2:
        return len
    else:
        if dy[len] == 0:
            dy[len] = DFS(len-2) + DFS(len-1)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))
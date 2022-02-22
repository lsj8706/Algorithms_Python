# 네트워크 선 자르기 (Top-Down: 재귀, 메모이제이션)
import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(len):
    if len == 1 or len == 2:
        return len
    else:
        if dy[len] == 0:
            dy[len] = DFS(len-2)+DFS(len-1)
        return dy[len]

if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1) # 메모이제이션을 위한 리스트
    print(DFS(n))





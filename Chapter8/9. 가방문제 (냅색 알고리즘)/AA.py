# 가방 문제 (냅색 알고리즘)
import sys
#sys.stdin = open("in2.txt", "rt")


if __name__ == "__main__":
    N, W  = map(int, input().split())
    dy = [0]*(W+1) # dy[j] 는 가방에 j무게만큼을 담을 수 있을 때 최대 가치
    for i in range(N):
        w, v = map(int, input().split())
        for j in range(w, W+1):
            dy[j] = max(dy[j], dy[j-w]+v)
    print(dy[W])
    
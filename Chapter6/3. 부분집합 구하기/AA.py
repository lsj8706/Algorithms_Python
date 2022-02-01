# 부분집합 구하기 (DFS)
import sys
sys.stdin = open("input.txt" ,"rt")

def subset(index):
    if index == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[index] = 1
        subset(index+1)
        ch[index] = 0
        subset(index+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1) # 0번째 인덱스는 사용 X
    subset(1)
# 알파코드 (DFS)
import sys
#sys.stdin = open("in2.txt", "rt")

def numToChr(num):
    return chr(num+64)

def DFS(L, pre):
    global cnt
    if L == len(code):
        if pre == 0:
            for x in res:
                if x != "":
                    print(x, end='')
            print()
            cnt += 1
    else:
        if pre == 0 and code[L] != 0:
            #채택
            res[L] = numToChr(code[L])
            DFS(L+1, 0)
            res[L] = ""
            #채택x
            DFS(L+1, code[L])
        else:
            if 10*pre+code[L] > 26:
                pass
            else:
                if pre != 0:
                    #무조건 채택
                    res[L] = numToChr(10*pre+code[L])
                    DFS(L+1, 0)
                    res[L] = ""

if __name__ == "__main__":
    code = list(map(int,list(input())))
    res = [""]*len(code)
    cnt = 0
    DFS(0, 0)
    print(cnt)
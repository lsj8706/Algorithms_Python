# 단어 찾기 (해쉬)
import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
n = 2*n - 1
dic = {}
for _ in range(n):
    word = input()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1


for key, val in dic.items():
    if val == 1:
        print(key)
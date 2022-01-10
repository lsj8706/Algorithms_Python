# 숫자만 추출
import sys
sys.stdin = open("input.txt", "rt")
s = input()
str = ""
for x in s:
    if x.isdecimal():
        str += x
num = int(str)
print(num)

# 약수 구하기
res = 0
for i in range(1, num+1):
    if num % i == 0:
        res += 1

print(res)

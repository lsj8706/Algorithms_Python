# 카드 역배치
import sys
sys.stdin = open("input.txt", "rt")
card = []
for i in range(1, 21):
    card.append(i)

for _ in range(0,10):
    a, b = map(int, input().split())
    temp = b
    for i in range(a, (a+b)//2 + 1):
        card[i-1], card[temp-1] = card[temp-1], card[i-1]
        temp -= 1

for x in card:
    print(x, end=' ')

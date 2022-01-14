# 스도쿠 검사
import sys
sys.stdin = open("input.txt", "rt")
sudoku = [list(map(int, input().split())) for _ in range(9)]
isSudoku = True
s1 = set()
s2 = set()
s3 = set()
s4 = set()
s5 = set()
s6 = set()
s7 = set()
s8 = set()
s9 = set()

for i in range(9):
    set1 = set(sudoku[0])
    if len(set1) != 9:
        isSudoku = False
    set2 = set()
    for j in range(9):
        set2.add(sudoku[j][i])
        if i < 3 and j < 3:
            s1.add(sudoku[i][j])
        elif i < 3 and j >= 3 and j < 6:
            s2.add(sudoku[i][j])
        elif i < 3 and j >= 6 and j < 9:
            s3.add(sudoku[i][j])
        elif i >= 3 and i < 6 and j < 3:
            s4.add(sudoku[i][j])
        elif i >= 3 and i < 6 and j >= 3 and j < 6:
            s5.add(sudoku[i][j])
        elif i >= 3 and i < 6 and j >= 6 and j < 9:
            s6.add(sudoku[i][j])
        elif i >= 6 and i < 9 and j < 3:
            s7.add(sudoku[i][j])
        elif i >= 6 and i < 9 and j >= 3 and j < 6:
            s8.add(sudoku[i][j])
        else:
            s9.add(sudoku[i][j])
    if len(set2) != 9:
        isSudoku = False

if len(s1) == len(s2) == len(s3) == len(s4) ==len(s5) ==len(s6) ==len(s7) ==len(s8) ==len(s9) == 9:
    pass
else:
    isSudoku = False

if isSudoku:
    print("YES")
else:
    print("NO")


import sys

arr = []  # (x1, y1, x2, y2) 형식의 원소를 가지는 배열 (리스트)
min_x, min_y = sys.maxsize, sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
max_x, max_y = -sys.maxsize, -sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값

xa, ya, xb, yb = map(int, input().split())
min_x, min_y = xa, ya
max_x, max_y = xb, yb
obstacle = [(xa, ya, xb, yb)]  # 싱크홀 좌표
n = int(input())  # 사각형 개수

offset_x, offset_y = 0, 0  # 좌표가 음수가 나올 수 있으므로 offset 설정

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_x, min_y = min(x1, min_x), min(y1, min_y)
    max_x, max_y = max(x2, max_x), max(y2, max_y)
    arr.append((x1, y1, x2, y2))

arr += obstacle
if min_x < 0:
    max_x += abs(min_x)
    offset_x += abs(min_x)
if min_y < 0:
    max_y += abs(min_y)
    offset_y += abs(min_y)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
min_w, min_h, max_w, max_h = max_x, max_y, 0, 0

for idx, (x1, y1, x2, y2) in enumerate(arr):
    for i in range(x1+offset_x, x2+offset_x):
        for j in range(y1+offset_y, y2+offset_y):
            if idx == n:  # 싱크홀 좌표일 때
                if not checked[i][j]:  # 덮어져 있는 영역이 True. False 영역을 구하는 것이 목표.
                    min_w, min_h = min(min_w, i), min(min_h, j)
                    max_w, max_h = max(max_w, i), max(max_h, j)
            else:  # 싱크홀을 덮는 영역일 때
                checked[i][j] = True

if max_w == 0:  # 모두 덮여져 있을 때
    print(0)
else:
    print((max_w-min_w+1)*(max_h-min_h+1))

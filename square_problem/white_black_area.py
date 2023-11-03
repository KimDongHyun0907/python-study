import sys

n = int(input())  # 사각형 개수

min_x, min_y = sys.maxsize, sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
max_x, max_y = -sys.maxsize, -sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
arr = []  # (x1, y1, x2, y2) 형식의 원소를 가지는 배열 (리스트)
offset_x, offset_y = 0, 0  # 좌표가 음수가 나올 수 있으므로 offset 설정

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_x, min_y = min(x1, min_x), min(y1, min_y)
    max_x, max_y = max(x2, max_x), max(y2, max_y)
    if i % 2 == 0:
        arr.append((x1, y1, x2, y2, 'w'))
    else:
        arr.append((x1, y1, x2, y2, 'b'))

if min_x < 0:
    max_x += abs(min_x)
    offset_x += abs(min_x)
if min_y < 0:
    max_y += abs(min_y)
    offset_y += abs(min_y)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt_w, cnt_b = 0, 0  # 흰색, 검은색 넓이
for x1, y1, x2, y2, color in arr:
    for i in range(x1+offset_x, x2+offset_x):
        for j in range(y1+offset_y, y2+offset_y):
            if color == 'w':
                checked[i][j] = 'w'
            else:
                checked[i][j] = 'b'

for area in checked:
    cnt_w += area.count('w')
    cnt_b += area.count('b')

print(cnt_w, cnt_b)

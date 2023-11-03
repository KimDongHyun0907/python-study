import sys

n = int(input())  # 사각형 개수

min_x, min_y = sys.maxsize, sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
max_x, max_y = -sys.maxsize, -sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
arr = []  # (x1, y1, x2, y2) 형식의 원소를 가지는 배열 (리스트)
offset_x, offset_y = 0, 0  # 좌표가 음수가 나올 수 있으므로 offset 설정

for _ in range(n):
    x, y, length = map(int, input().split())
    min_x, min_y = min(x, min_x), min(y, min_y)
    max_x, max_y = max(x+length, max_x), max(y+length, max_y)
    arr.append((x, y, x+length, y+length))

if min_x < 0:
    max_x += abs(min_x)
    offset_x += abs(min_x)
if min_y < 0:
    max_y += abs(min_y)
    offset_y += abs(min_y)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt = 0  # 직사각형 넓이
for x1, y1, x2, y2 in arr:
    for i in range(x1+offset_x, x2+offset_x):
        for j in range(y1+offset_y, y2+offset_y):
            if not checked[i][j]:
                checked[i][j] = True
                cnt += 1

print(cnt)

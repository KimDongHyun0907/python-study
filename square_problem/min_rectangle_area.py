import sys

n = int(input())  # 사각형 개수

min_x, min_y = sys.maxsize, sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값
max_x, max_y = -sys.maxsize, -sys.maxsize  # n개의 사각형 중 x 좌표와 y 좌표의 최솟값

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_x, min_y = min(x1, min_x), min(y1, min_y)
    max_x, max_y = max(x2, max_x), max(y2, max_y)

print((max_x-min_x)*(max_y-min_y))

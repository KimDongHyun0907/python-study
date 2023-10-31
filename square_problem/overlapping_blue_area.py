import sys
input = sys.stdin.readline

n = int(input())
min_x, min_y = sys.maxsize, sys.maxsize
max_x, max_y = -sys.maxsize, -sys.maxsize
arr = []
offset_x, offset_y = 0, 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_x, min_y = min(x1, min_x), min(y1, min_y)
    max_x, max_y = max(x2, max_x), max(y2, max_y)
    if i%2 == 0:
        arr.append((x1, y1, x2, y2, 'r'))
    else:
        arr.append((x1, y1, x2, y2, 'b'))

if min_x < 0 or min_y < 0:
    max_x += abs(min_x)
    max_y += abs(min_y)
    offset_x += abs(min_x)
    offset_y += abs(min_y)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt = 0
for x1, y1, x2, y2, color in arr:
    for i in range(x1+offset_x, x2+offset_x):
        for j in range(y1+offset_y, y2+offset_y):
            if color == 'r':
                checked[i][j] = 'r'
            else:
                checked[i][j] = 'b'

for i in checked:
    cnt += i.count('b')
print(cnt)

import sys
input = sys.stdin.readline

min_val = sys.maxsize
max_x, max_y = -sys.maxsize, -sys.maxsize
arr = []
offset = 0

for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    min_val = min(x1, y1, min_val)
    max_x, max_y = max(x2, max_x), max(y2, max_y)
    arr.append((x1, y1, x2, y2, i))

if min_val < 0:
    max_x += abs(min_val)
    max_y += abs(min_val)
    offset += abs(min_val)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt = 0 
for x1, y1, x2, y2, idx in arr:
    for i in range(x1+offset, x2+offset):
        for j in range(y1+offset, y2+offset):
            if idx == 1:
                if checked[i][j]:
                    checked[i][j] = False
            else:
                checked[i][j] = True

max_h, max_w, min_h, min_w = -1, -1, max_y, max_x
for i in range(max_x+1):
    for j in range(max_y+1):
        if checked[i][j]:
            max_h = max(max_h, j)
            max_w = max(max_w, i)
            min_h = min(min_h, j)
            min_w = min(min_w, i)

if max_h < 0:
    print(0)
else:
    print((max_w-min_w+1)*(max_h-min_h+1))

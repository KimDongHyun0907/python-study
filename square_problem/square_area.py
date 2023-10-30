import sys
input = sys.stdin.readline

n = int(input())
offset = 0
min_val = sys.maxsize
max_x, max_y = -sys.maxsize, -sys.maxsize
arr = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_val = min(x1, x2, y1, y2, min_val)
    max_x = max(x1, x2, max_x)
    max_y = max(y1, y2, max_y)
    arr.append([x1, y1, x2, y2])

if min_val < 0:
    max_x += abs(min_val)
    max_y += abs(min_val)
    offset += abs(min_val)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt = 0
for x1, y1, x2, y2 in arr:
    for i in range(x1+offset, x2+offset):
        for j in range(y1+offset, y2+offset):
            if not checked[i][j]:
                checked[i][j] = True
                cnt += 1
print(cnt)

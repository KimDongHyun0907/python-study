import sys
input = sys.stdin.readline

min_val = sys.maxsize
max_x, max_y = -sys.maxsize, -sys.maxsize
arr = []
offset = 0

n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    min_val = min(x1, y1, x2, y2, min_val)
    max_x, max_y = max(x1, x2, max_x), max(y1, y2, max_y)
    arr.append((x1, y1, x2, y2))

if min_val < 0:
    max_x += abs(min_val)
    max_y += abs(min_val)
    offset += abs(min_val)

checked = [[False for _ in range(max_y+1)] for _ in range(max_x+1)]
cnt = 0
for i in range(n):
    for j in range(arr[i][0], arr[i][2]):
        for k in range(arr[i][1], arr[i][3]):
            if i == n-1:
                if checked[j][k]:
                    cnt -= 1
            elif not checked[j][k]:
                checked[j][k] = True
                cnt += 1
print(cnt)

import sys

n = int(input())
curr = 0
max_size = -sys.maxsize
min_size = sys.maxsize
arr = []

for _ in range(n):
    a, b = input().split()
    a = int(a)
    arr.append((a, b))
    if b == 'R':
        max_size = max(max_size, curr+a-1)
        curr += a-1
    else:
        min_size = min(min_size, curr-a+1)
        curr -= a-1

curr = 0
if min_size < 0:
    max_size += abs(min_size)
    curr = abs(min_size)

color_check = [[0, 0, 0] for _ in range(max_size+1)]

for x, y in arr:
    if y == 'R':
        for i in range(curr, curr+x):
            color_check[i][1] += 1
            color_check[i][2] = 'b'
        curr += x-1
    else:
        for i in range(curr-x+1, curr+1):
            color_check[i][0] += 1
            color_check[i][2] = 'w'
        curr -= x-1

white, black, gray = 0, 0, 0
for x, y, z in color_check:
    if x >= 2 and y >= 2:
        gray += 1
    else:
        if z == 'b':
            black += 1
        else:
            white += 1

print(white, black, gray)

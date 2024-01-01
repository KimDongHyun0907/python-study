def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

d1, d2 = divmod(k-1, n)
x, y = [(0, d2), (d2, n-1), (n-1, n-1-d2), (n-1-d2, 0)][d1]

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
cnt = 0
while in_range(x, y):
    if arr[x][y] == '/':
        x += dx[d1]
        y += dy[d1]
        d1 = d1+1 if d1 % 2 == 0 else d1-1
        
    else:
        x += dx[d1]*(-1)
        y += dy[d1]*(-1)
        d1 = 3 -d1

    cnt += 1

print(cnt)

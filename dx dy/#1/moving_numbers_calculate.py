def in_range(x,y):
    return 0<=x<n and 0<=y<n

n, m = map(int,input().split())
x, y = map(int,input().split())
commands = input()
arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
i=0
ans = arr[x-1][y-1]
x, y = x-1, y-1
isplus = True

for c in commands:
    if c == 'R':
        i=(i+1)%4
    elif c == 'L':
        i=(i+3)%4
    else:
        nx, ny = x+dxs[i], y+dys[i]
        if in_range(nx, ny):
            if isplus:
                ans += arr[nx][ny]
                isplus = False
            else:
                ans -= arr[nx][ny]
                isplus = True
            x, y = nx, ny
print(ans)
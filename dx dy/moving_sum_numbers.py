def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

n, t = map(int, input().split())
command = input()

arr = [list(map(int, input().split())) for _ in range(n)]
x, y, d = n//2, n//2, 0
ans = arr[x][y]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

for val in command:
    if val == 'L':
        d = (d+1)%4
    
    elif val == 'R':
        d = (d+3)%4

    else:
        new_x, new_y = x+dx[d], y+dy[d]
        if in_range(new_x, new_y):
            x, y = new_x, new_y
            ans += arr[x][y]

print(ans)
        

def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n

n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
    cnt = 0
    
    for d in range(4):
        new_x, new_y = x-1+dx[d], y-1+dy[d]
        if in_range(new_x, new_y) and arr[new_x][new_y] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)

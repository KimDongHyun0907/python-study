def in_range(x, y):
    return 0<=x<n and 0<=y<m

n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

d = [(0,1), (1,0), (0, -1), (-1, 0)]
dir_num = 0
x, y = 0, 0
arr[x][y] = 1

for i in range(2, n*m+1):
    dx, dy = d[dir_num]
    new_x, new_y = x+dx, y+dy
    
    if not in_range(new_x, new_y) or arr[new_x][new_y]:
        dir_num = (dir_num+1)%4
        dx, dy = d[dir_num]
    
    x, y = x+dx, y+dy
    arr[x][y] = i

for row in arr:
    print(*row)
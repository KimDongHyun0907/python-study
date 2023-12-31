def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m

n,m=map(int,input().split())
arr=[[0 for _ in range(m)] for _ in range(n)]

x, y, d = 0, 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(1, n*m+1):
    arr[x][y] = i
    new_x, new_y = x+dx[d], y+dy[d]

    if in_range(new_x, new_y) and arr[new_x][new_y] == 0:
        x, y = new_x, new_y
    
    else:
        d = (d+1)%4
        x, y = x+dx[d], y+dy[d]

for row in arr:
    print(*row)

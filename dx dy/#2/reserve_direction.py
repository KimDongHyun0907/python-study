def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

n, m=map(int, input().split())  # n은 배열의 행과 열. m은 반복 횟수

arr = [[0]*n for _ in range(n)]
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1] # 우, 하, 상, 좌

x, y = map(int, input().split())
d = int(input())
print('='*20)
for i in range(m):
    nx, ny = x+dxs[d], y+dys[d]

    if not in_range(nx, ny):
        d = 3-d  # 방향 바꾸기
        nx, ny = x+dxs[d], y+dys[d]
    
    x, y = nx, ny
    print(x, y)
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
cnts = [0, 0, 0, 0, 0]

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        cnts[cnt] += 1

for idx in range(1, 5):
    print(f'인접한 1이 {idx}개인 위치는 {cnts[idx]}')

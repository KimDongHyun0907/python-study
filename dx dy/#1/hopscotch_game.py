def in_range(x, y):
    return 0 <= x < n and 0 <=y < n

n,m = map(int, input().split())
arr = [[0] * n for _ in range(n)]
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
sum_cnt = 0
for _ in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

    cnt = sum(1 for dx, dy in zip(dxs, dys) if in_range(r-1+dx, c-1+dy) and arr[r-1+dx][c-1+dy] == 1)
    
    if cnt == 4:
        sum_cnt += 1

print(f'점령한 땅의 개수는 {sum_cnt}')
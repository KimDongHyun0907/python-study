n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

d = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 아래 왼 위 오른

d_num = (k - 1) // n
x, y = [(0, k - 1), 
            (k - n - 1, n - 1), 
            (n - 1, (n - 1) - (k - 1) % n), 
            ((n - 1) - (k - 1) % n, 0)][d_num]

cnt = 0
while 0 <= x < n and 0 <= y < n:
  if arr[x][y] == '\\':
    d_num = 3 - d_num

  else:
    d_num = d_num ^ 1
  
  dx, dy = d[d_num]
  x, y = x + dx, y + dy

  cnt += 1

print(cnt)
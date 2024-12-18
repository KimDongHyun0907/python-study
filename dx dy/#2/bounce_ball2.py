n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

if k <= n:
  x, y = 0, k - 1
  d_num = 0

elif k <= 2 * n:
  x, y = k - n - 1, n - 1
  d_num = 1

elif k <= 3 * n:
  x, y = n - 1, (n - 1) - (k - 1) % n
  d_num = 2

else:
  x, y = (n - 1) - (k - 1) % n, 0
  d_num = 3

cnt = 0
while 0 <= x < n and 0 <= y < n:
  if arr[x][y] == '\\':
    d_num = 3 - d_num

  else:
    d_num = d_num + 1 if d_num % 2 == 0 else d_num - 1
  
  dx, dy = d[d_num]
  x, y = x + dx, y + dy

  cnt += 1

print(cnt)
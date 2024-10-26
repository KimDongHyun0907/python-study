def round_fun(num, clockwise, x, y, i):
  d_num = num
  for _ in range(n * m):
    arr[x][y] = chr(ord('A') + i % 26)
    dx, dy = d[d_num]
    i += 1

    if not (0 <= x + dx < n and 0 <= y + dy < m) or arr[x + dx][y + dy] != 0:
      d_num = (d_num + clockwise) % 4
      dx, dy = d[d_num]
    
    x, y = x + dx, y + dy

  for rows in arr:
    print(*rows)

n, m = map(int, input().split())
round_num = int(input())
arr = [[0] * m for _ in range(n)]
x, y, i = 0, 0, 0

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

if round_num == 0:
  round_fun(round_num, 1, x, y, i)

else:
  round_fun(round_num, 3, x, y, i)
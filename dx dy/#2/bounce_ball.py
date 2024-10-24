n = int(input())
arr = [list(input()) for _ in range(n)]

d = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 아래 왼 위 오른

for i in range(n):
  x, y, d_num, cnt = 0, i, 0, 0
  curr_x, curr_y = x, y

  while 0 <= curr_x < n and 0 <= curr_y < n:
    d_num = 3 - d_num if arr[curr_x][curr_y] == '\\' else d_num ^ 1
    dx, dy = d[d_num]
    curr_x, curr_y = curr_x + dx, curr_y + dy
    cnt += 1

  print(f'({x+1}, {y+1}) {cnt}')
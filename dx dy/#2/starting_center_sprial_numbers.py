def fill_out_numbers(number, n, step, x, y, first_d_num):
  d_num = first_d_num
  while number <= n * n:
    for _ in range(2):
      for _ in range(step):
        if number > n * n:
          break
        dx, dy = d[d_num]
        x, y = x + dx, y + dy
        arr[x][y] = number
        number += 1
      d_num = (d_num + first_d_num + 1) % 4
    step += 1

n = int(input())
arr = [[0] * n for _ in range(n)]
is_clockwise = int(input())  # 0 반시계, 1 시계

x, y = n // 2, n // 2
arr[x][y] = 1
d = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 오른 위 왼 아래
step, number = 1, 2

fill_out_numbers(number, n, step, x, y, 2) if is_clockwise else fill_out_numbers(number, n, step, x, y, 0)
  
for row in arr:
  print(*row)


'''
n=3
11 R 12 U 02 L 01 L 00 D 10 D 20 R 21 R 22
RU LLDD RR

n=5
22 R 23 U 13 L 12 L 11 D 21 D 31 R 32 R 33 R 34 U 24 U 14 U
04 L 03 L 02 L 01 L 00 D 10 D 20 D 30 D 40 R 41 R 42 R 43 R 44
RU LLDD RRRUUU LLLLDDDD RRRR

'''
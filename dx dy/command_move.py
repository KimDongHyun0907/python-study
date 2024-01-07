x, y = map(int, input('초기 위치: ').split())
curr_d = input('방향 입력: ')
ds = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
d = ds[curr_d]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

inp_ds = input()
for val in inp_ds:
    if val == 'L':
        d = (d-1+4) % 4
    elif val == 'R':
        d = (d+1) % 4
    else:
        x, y = x+dx[d], y+dy[d]

print(x, y)

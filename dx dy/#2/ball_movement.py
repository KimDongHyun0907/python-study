def in_range(x, y):
    return 0<x<=n and 0<y<=n

n, t = map(int, input().split()) # n: 격자 크기, t: 시간 (초)
curr_x, curr_y = map(int, input().split()) # 현재 위치 (x, y)
curr_dir = input() # 현재 방향

dir_map = {'R':0, 'D':1, 'U':2, 'L':3}
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]  # 우, 하, 상, 좌

dir_index = dir_map[curr_dir]
cnt = 0
for _ in range(t):
    new_x, new_y = curr_x+dxs[dir_index], curr_y+dys[dir_index]
    if not in_range(new_x, new_y):
        dir_index = 3 - dir_index
        cnt += 1
    else:
        curr_x, curr_y = new_x, new_y

print(f'현재 위치는 ({curr_x}, {curr_y})')
print(f'벽에 부딪힌 횟수 {cnt}')

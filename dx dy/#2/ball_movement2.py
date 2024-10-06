def in_range(x, y):
    return 0<x<=n and 0<y<=n

n, t = map(int, input().split()) # n: 격자 크기, t: 시간 (초)
curr_x, curr_y = map(int, input().split()) # 현재 위치 (x, y)
curr_dir = input() # 현재 방향

dir_map = {'R': (0,1), 'D': (1,0), 'U':(-1,0), 'L':(0, -1)}
dx, dy = dir_map[curr_dir]
cnt = 0
for _ in range(t):
    new_x, new_y = curr_x+dx, curr_y+dy
    if not in_range(new_x, new_y):
        dx, dy = -dx, -dy
        cnt += 1
    else:
        curr_x, curr_y = new_x, new_y

print(f'현재 위치는 ({curr_x}, {curr_y})')
print(f'벽에 부딪힌 횟수 {cnt}')
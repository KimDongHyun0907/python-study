dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
d_map = {'Right':0, 'Down':1, 'Left':2, 'Up':3}

curr_dir = 'Left'
move_dir = d_map[curr_dir]

x, y = map(int, input().split())
new_x, new_y = x + dxs[move_dir], y + dys[move_dir]

print(new_x, new_y)
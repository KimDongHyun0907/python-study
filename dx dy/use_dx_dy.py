num = int(input('숫자를 입력하세요: '))
pos_x, pos_y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

pos_x, pos_y = pos_x+dx[num], pos_y+dy[num]

print(f'이동한 후 위치는 {pos_x}, {pos_y}이다.')

num = int(input('숫자를 입력하세요: '))
pos_x, pos_y = 0, 0

if num == 0:
    pos_y += 1
elif num == 1:
    pos_x += 1
elif num == 2:
    pos_y -= 1
else:
    pos_x -= 1

print(f'이동한 후 위치는 {pos_x}, {pos_y}이다.')

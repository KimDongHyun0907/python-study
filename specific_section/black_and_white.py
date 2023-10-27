# 미완성

import sys

n = int(input())
distance_arr = []
point = 0
min_point = sys.maxsize
max_point = -sys.maxsize

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    if direction == 'R':
        distance_arr.append([point, point+distance, direction])
        point += distance
        max_point = max(point, max_point)
    else:
        distance_arr.append([point-distance, point, direction])
        point -= distance
        min_point = min(point, min_point)

if min_point < 0:
    offset = min_point*(-1)
    max_point += offset
    distance_arr = list(map(lambda x: [x[0]+offset, x[1]+offset, x[2]], distance_arr))

color_check = [[0, 0, 0] for _ in range(max_point+1)]  # w, g, b

for x, y, z in distance_arr:
    if z == 'R':
        for i in range(x, y+1):
            color_check[i][0] += 1
    else:
        for i in range(x, y+1):
            color_check[i][2] += 1

print(color_check)
print(distance_arr)

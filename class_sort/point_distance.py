x, y = map(int, input().split())
n = int(input())

points = []
for _ in range(n):
    new_x, new_y = map(int, input().split())
    distance = (((new_x-x)**2)+((new_y-y)**2))**0.5
    points.append((new_x, new_y, distance))

points.sort(key=lambda x: x[2])
for idx, (x, y, _) in enumerate(points, start=1):
    print(f'{idx}. ({x}, {y})')

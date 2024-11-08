n = int(input())
x, y = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

for _ in range(n):
    d, distance = input().split()
    distance = int(distance)
    x, y = x+dx[directions[d]]*distance, y+dy[directions[d]]*distance

print(x, y)

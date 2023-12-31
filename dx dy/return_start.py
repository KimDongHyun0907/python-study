n = int(input())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북 동 남 서
direction = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
x, y, cnt, ans = 0, 0, 0, -1

for _ in range(n):
    d, m = input().split()
    m = int(m)

    for _ in range(m):
        x, y = x+dx[direction[d]], y+dy[direction[d]]
        cnt += 1

        if x == 0 and y == 0:
            ans = cnt
            break
        
    if ans != -1:
        break

print(ans)

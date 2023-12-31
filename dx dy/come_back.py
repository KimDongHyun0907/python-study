command = input()

x, y, d, ans, cnt = 0, 0, 0, -1, 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for s in command:
    if s == 'F':
        x += dx[d]
        y += dy[d]
    
    elif s == 'R':
        d = (d+1)%4
    
    else:
        d = (d-1+4)%4
    
    cnt += 1
    if x == 0 and y == 0:
        ans = cnt
    
    if ans != -1:
        break

print(ans)

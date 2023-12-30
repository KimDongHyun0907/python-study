s=input()
x,y=0,0
dir=[(0,1),(1,0),(0,-1),(-1,0)]
dir_num=0
for val in s:
    if val=='L':
        dir_num=(dir_num-1)%4
    elif val=='R':
        dir_num=(dir_num+1)%4
    else:
        x+=dir[dir_num][0]
        y+=dir[dir_num][1]

print(x, y)

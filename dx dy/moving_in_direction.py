n=int(input())
x,y=0,0
dir=[(-1,0), (1,0), (0,1), (0,-1)]
for _ in range(n):
    d, m = input().split()
    m=int(m)
    if d=='W':
        dnum=0
    elif d=='E':
        dnum=1
    elif d=='N':
        dnum=2
    else:
        dnum=3
    
    x+=dir[dnum][0]*m
    y+=dir[dnum][1]*m

print(x,y)

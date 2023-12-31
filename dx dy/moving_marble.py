n,t=map(int,input().split())
r,c,d=input().split()
r,c=int(r),int(c)

dir_list=[(0,1),(1,0),(-1,0),(0,-1)]
if d=='L':
    dir_num=3
elif d=='R':
    dir_num=0
elif d=='U':
    dir_num=2
else:
    dir_num=1

for i in range(t):
    new_r=r+dir_list[dir_num][0]
    new_c=c+dir_list[dir_num][1]
    
    if new_r==0 or new_c==0 or new_r==n+1 or new_c==n+1:
        dir_num=3-dir_num
    
    else:
        r=new_r
        c=new_c

print(r,c)

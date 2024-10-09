def in_range(x,y):
  return 0<=x<n and 0<=y<n

n=int(input())
arr=[list(input()) for _ in range(n)]
k=int(input())

if (k-1)//n==0:
  x,y=0,k-1
elif (k-1)//n==1:
  x,y=(k-1)%n, n-1
elif (k-1)//n==2:
  x,y=n-1, (n-1)-(k-1)%n
else:
  x,y=(n-1)-(k-1)%n, 0

# x,y=0,1
d = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌
dir_num=0
cnt=0

while True:
  if arr[x][y]=='\\':
    dir_num=3-dir_num
    dx,dy=d[dir_num]
    x,y=x-dx,y-dy

  else:
    dir_num = (dir_num+1)%4
    dx,dy=d[dir_num]
    x,y=x-dx,y-dy
  print(dir_num,x,y)
  if not in_range(x,y):
    print(cnt)
    break
  
  cnt+=1
  

'''
\
0 3
1 2
2 1
3 0

/
0 1
1 2
2 3
3 0

3
/\\
\\\
/\/
2

0 01
3 02
0 12
3 13

'''
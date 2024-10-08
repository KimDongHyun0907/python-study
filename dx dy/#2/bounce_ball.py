n=int(input())
arr=[list(input()) for _ in range(n)]

x,y=0,1
d = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌
dir_num=0
cnt=0

if arr[x][y]=='\\':
  cnt+=1
  dx,dy=d[(dir_num+1)%4]
  x,y=x+dx,y+dy
  

'''
\
0 1
1 2
2 3
3 0
'''
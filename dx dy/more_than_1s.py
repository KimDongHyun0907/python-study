n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

direct_list=[(0,1),(1,0),(0,-1),(-1,0)]
total_cnt=0
for x in range(n):
    for y in range(n):
        cnt=0
        for i in range(4):
            new_x=x+direct_list[i][0]
            new_y=y+direct_list[i][1]
            if in_range(new_x,new_y) and arr[new_x][new_y]==1:
                cnt+=1
        if cnt>=3:
            total_cnt+=1

print(total_cnt)

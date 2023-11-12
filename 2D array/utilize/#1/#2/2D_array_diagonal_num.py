n,m=map(int,input().split())
arr=[[0 for _ in range(m)] for _ in range(n)]

num=1
for i in range(m):
    j=0
    while True:
        arr[j][i]=num
        num+=1
        j+=1
        i-=1
        if i<0 or i>m-1 or j<0 or j>n-1: break
    
for i in range(1,n):
    j=m-1
    while True:
        arr[i][j]=num
        num+=1
        i+=1
        j-=1
        if i<0 or i>n-1 or j<0 or j>m-1: break

for i in arr:
    for j in i:
        print(j,end=' ')
    print()

n,m=map(int,input().split())
arr=[[0 for _ in range(n)] for _ in range(n)]

num=1
for _ in range(m):
    a,b=map(int,input().split())
    arr[a-1][b-1]=num
    num+=1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()

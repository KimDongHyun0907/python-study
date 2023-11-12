n,m=map(int,input().split())

arr=[[0 for _ in range(m)] for _ in range(n)]

cnt,num=1,1

for i in range(m-1,-1,-1):
    if cnt%2==1:
        for j in range(n-1,-1,-1):
            arr[j][i]=num
            num+=1
    else:
        for j in range(n):
            arr[j][i]=num
            num+=1
    cnt+=1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()

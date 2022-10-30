n,m=map(int,input().split())

arr=[[0 for _ in range(m)] for _ in range(n)]

cnt=1
for i in range(m-1,-1,-1):
    if i%2==1:
        for j in range(n-1,-1,-1):
            arr[j][i]=cnt
            cnt+=1
    else:
        for j in range(n):
            arr[j][i]=cnt
            cnt+=1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()

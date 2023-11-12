n,m=map(int,input().split())

arr=[[0 for _ in range(m)] for _ in range(n)]

num=0
cnt=0
for i in range(m):
    for j in range(n):
        arr[num][i]=cnt
        if i%2==0: num+=1
        else: num-=1
        cnt+=1
    if i%2==0: num-=1
    else: num+=1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()

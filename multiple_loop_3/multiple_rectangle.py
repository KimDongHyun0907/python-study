inp=input().split()

n,m=int(inp[0]),int(inp[1])
for i in range(1,n+1):
    for j in range(i,i*(m+1),i):
        print(j,end=' ')
    print()

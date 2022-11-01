n=int(input())

arr=[[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if j==0 or j==i:
            print(arr[i][j],end=' ')
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
            print(arr[i][j],end=' ')
    print()

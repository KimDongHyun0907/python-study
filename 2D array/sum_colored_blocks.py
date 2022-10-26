n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
sum_val=0
for i in range(n):
    for j in range(n-1-i,n):
        sum_val+=arr[i][j]
print(sum_val)

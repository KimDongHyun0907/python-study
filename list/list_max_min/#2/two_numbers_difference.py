n=int(input())
arr=list(map(int,input().split()))

max_val=arr[n-1]-arr[0]
min_val=arr[1]-arr[0]
for i in range(2,n):
    if arr[i]-arr[i-1]:
        min_val=min(min_val,arr[i]-arr[i-1])

print(max_val,min_val)

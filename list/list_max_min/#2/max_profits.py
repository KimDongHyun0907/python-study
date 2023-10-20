n=int(input())
arr=list(map(int,input().split()))

min_val=arr[0]
ans=0
for i in range(1,n):
    ans=max(arr[i]-min_val,ans)
    min_val=min(arr[i],min_val)
print(ans)

n=int(input())
arr=list(map(int,input().split()))

arr.sort()
max_val=0
for i in range(n//2):
    val=arr[i]+arr[n-i-1]
    max_val=max(max_val,val)
print(max_val)

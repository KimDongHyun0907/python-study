arr=list(map(int,input().split()))

sum_val=0
for i in range(0,len(arr),2):
    sum_val+=arr[i]

print(sum_val)

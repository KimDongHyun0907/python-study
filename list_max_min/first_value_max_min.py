# 최댓값
arr=list(map(int,input().split()))

max_val=arr[0]
for i in arr[1:]:
    if max_val<i:
        max_val=i

print(max_val)

# 최솟값
arr=list(map(int,input().split()))

min_val=arr[0]
for i in arr[1:]:
    if min_val>i:
        min_val=i

print(min_val)

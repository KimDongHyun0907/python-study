# 최댓값
arr=list(map(int,input().split()))

max_val=0
for i in arr:
    if max_val<i:
        max_val=i

print(max_val)

# 최솟값
arr=list(map(int,input().split()))

min_val=999999
for i in arr:
    if min_val>i:
        min_val=i

print(min_val)

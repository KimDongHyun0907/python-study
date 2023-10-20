# 최댓값
import sys

arr=list(map(int,input().split()))

max_val=-sys.maxsize
for i in arr:
    if max_val<i:
        max_val=i

print(max_val)

# 최솟값
import sys

arr=list(map(int,input().split()))

min_val=sys.maxsize
for i in arr:
    if min_val>i:
        min_val=i

print(min_val)

arr=list(map(int,input().split()))

max_val=max(arr)
count_list=[0 for _ in range(max_val+1)]

for i in arr:
    count_list[i]+=1

ans=-1
for i in range(max_val,0,-1):
    if count_list[i]==1:
        ans=i
        break
print(ans)

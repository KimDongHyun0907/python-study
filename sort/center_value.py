n=int(input())
arr=list(map(int,input().split()))
ans=[]

for i in range(n):
    ans.append(arr[i])
    ans.sort()
    if i%2==0: print(ans[i//2],end=' ')
    else: print((ans[i//2]+ans[i//2+1])//2,end=' ')

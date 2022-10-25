n=int(input())
arr=list(map(int,input().split()))
a,b=0,1001
for i in arr:
    if i<n and i>a:
        a=i
    elif i>n and i<b:
        b=i

if a==0:
    a=-1
if b==1001:
    b=-1

print(a,b)

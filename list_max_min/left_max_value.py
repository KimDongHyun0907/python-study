n=int(input())
arr=list(map(int,input().split()))

arr2=[1]
j=0
for i in range(1,n):
    if arr[i]>arr[arr2[j]-1]:
        arr2.append(i+1)
        j+=1

for i in arr2[::-1]:
    print(i,end=' ')

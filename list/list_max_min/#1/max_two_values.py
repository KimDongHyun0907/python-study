arr=list(map(int,input().split()))

if arr[0]>arr[1]:
    max1,max2=arr[0],arr[1]
else:
    max1,max2=arr[1],arr[0]

for i in arr[2:]:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2:
        max2=i
    
print(max1,max2)

a,b=map(int,input().split())
arr=[]
arr.append(a)
arr.append(b)

for i in range(3,11):
    arr.append(3*arr[-1]+2*arr[-2])
print(arr)

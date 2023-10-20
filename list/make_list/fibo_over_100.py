a,b=map(int,input().split())
arr=[]
arr.append(a)
arr.append(b)

while arr[-1]<=100:
    arr.append(arr[-1]+arr[-2])

print(arr)

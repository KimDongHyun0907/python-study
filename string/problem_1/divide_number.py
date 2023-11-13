n=int(input())
arr=list(map(int,input().split()))
m=int(input())
num=''
for elem in arr:
    num+=str(elem)
for i in range(0,len(num),m):
    if i+m>len(num):
        print(num[i:len(num)])
    else: 
        print(num[i:i+m])

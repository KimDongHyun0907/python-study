inp=input().split()
a,b=int(inp[0]),int(inp[1])

if a%2==0:
    i=a
else:
    i=a+1

while i<=b:
    print(i,end=' ')
    i+=2

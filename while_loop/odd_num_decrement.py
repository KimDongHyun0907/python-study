inp=input().split()
a,b=int(inp[0]),int(inp[1])

if b%2==1:
    i=b
else:
    i=b-1

while i>=a:
    print(i,end=' ')
    i-=2

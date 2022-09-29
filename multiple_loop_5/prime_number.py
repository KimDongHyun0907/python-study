inp=input().split()
a,b=int(inp[0]),int(inp[1])

for i in range(a,b+1):
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime==True:
        print(i,end=' ')

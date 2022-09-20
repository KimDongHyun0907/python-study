inp=input().split()
a,b=int(inp[0]),int(inp[1])

prod=1
for i in range(a,b+1):
    prod*=i

print(prod)

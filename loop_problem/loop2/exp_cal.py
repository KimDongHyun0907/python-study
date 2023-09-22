inp=input().split()
a,b=int(inp[0]),int(inp[1])

prod=1
for i in range(b):
    prod*=a
print(prod)

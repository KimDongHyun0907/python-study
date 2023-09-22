inp=input().split()
a,b,n=int(inp[0]),int(inp[1]),int(inp[2])

print(f'{a//b}.',end='')
a%=b
for _ in range(n):
    a*=10
    print(a//b,end='')
    a%=b

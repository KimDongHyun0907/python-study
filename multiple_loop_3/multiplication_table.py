inp=input().split()
a,b=int(inp[0]),int(inp[1])

for i in range(2,10,2):
    for j in range(a,b+1):
        print(f'{j}*{i}={j*i}',end=' ')
        if j==b: continue
        print('/',end=' ')
    print()

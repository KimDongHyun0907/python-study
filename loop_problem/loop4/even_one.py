inp=input().split()
a,b=int(inp[0]),int(inp[1])

booltype=False
for i in range(a,b+1):
    if i%2==0:
        booltype=True

if booltype==True:
    print('even exists')
else:
    print('even not exists')

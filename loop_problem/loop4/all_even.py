inp=input().split()
a,b=int(inp[0]),int(inp[1])

booltype=True
for i in range(a,b+1):
    if i%2!=0:
        booltype=False

if booltype==True:
    print('all even')
else:
    print('not all even')

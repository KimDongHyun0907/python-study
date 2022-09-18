inp=input().split()
a,b=int(inp[0]),int(inp[1])

for i in range(a,b+1):
    print(i,end=' ')

print()
for i in range(a,b+1):
    if i%2==0 and i%3==0 :
        print(23,end=' ')
    elif i%2==0:
        print(2,end=' ')
    elif i%3==0:
        print(3,end=' ')
    else:
        print(0,end=' ')

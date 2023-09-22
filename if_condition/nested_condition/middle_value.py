inp=input().split()
a,b,c=int(inp[0]),int(inp[1]),int(inp[2])

"""
b<a<c
c<a<b

a<b<c
c<b<a

a<c<b
b<c<a
"""

if a>b:
    if c>a:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)

else:
    if a>c:
        print(a)
    elif c>b:
        print(b)
    else:
        print(c)

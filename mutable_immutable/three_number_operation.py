def operation(n1,n2,n3):
    if n1>n2:
        if n2>n3:
            return n1+n2, n2+n3
        else:
            return n3+n1, n1+n2
    elif n1>n3:
        if n3>n2:
            return n1+n3, n3+n2
        else:
            return n2+n1, n1+n3
    if n2>n1:
        if n2>n3:
            return n2+n3, n3+n1
        else:
            return n3+n2, n2+n1


a,b,c=map(int,input().split())
m1, m2=operation(a,b,c)
print(m1,m2)

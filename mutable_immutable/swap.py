def swap(a,b):
    a,b=b,a
    print(a,b)

n,m=1,2
swap(n,m)
print(n,m)

----------------------------

def swap(a,b):
    a,b=b,a
    return a,b 

n,m=1,2
n,m=swap(n,m)
print(n,m)

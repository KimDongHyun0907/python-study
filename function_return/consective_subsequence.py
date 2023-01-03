n1,n2=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def is_same(i):
    for j in range(n2):
        if b[j]!=a[i+j]:
            return False
    return True

def is_subsequence():
    for i in range(n1-n2+1):
        if is_same(i):
            return True
    return False

if is_subsequence(): print('Yes')
else: print('No')

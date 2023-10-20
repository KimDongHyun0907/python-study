n=int(input())

booltype=False
for i in range(2,n):
    if n%i==0:
        booltype=True

if booltype==True:
    print('Yes')
else:
    print('No')

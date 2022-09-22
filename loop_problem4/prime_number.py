n=int(input())

booltype=True
for i in range(2,n):
    if n%i==0:
        booltype=False

if booltype==True:
    print('Yes')
else:
    print('No')

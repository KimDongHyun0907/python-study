n=int(input())

cnt=0
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            print('*',end=' ')
    
    else:
        for j in range(n):
            if j==0 or j==n-1:
                print('*',end=' ')
            elif j>cnt:
                print(' ',end=' ')
            else:
                print('*',end=' ')
        cnt+=1
    print()

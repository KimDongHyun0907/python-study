n=int(input())

cnt=n+1
for i in range(2*n-1):
    if i<n:
        cnt-=1
    else:
        cnt+=1

    for j in range(cnt):
        print('*',end=' ')
    print()

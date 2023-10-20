n=int(input())

cnt=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==1:
            print(cnt,end=' ')
            if j==n:
                cnt+=n
            else:
                cnt+=1
        else:
            print(cnt,end=' ')
            if j==n:
                cnt+=n
            else:
                cnt-=1
    print()

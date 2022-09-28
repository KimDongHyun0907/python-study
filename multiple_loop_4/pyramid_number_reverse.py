n=int(input())

cnt=1
blank=0
for i in range(n):
    for j in range(n):
        if j<blank:
            print(' ',end=' ')
        else:
            print(cnt,end=' ')
            cnt+=1
            if cnt==10: 
                cnt=1
    blank+=1
    print()

n=int(input())

blank=0
cnt=ord('A')

for i in range(n):
    for j in range(n):
        if j<blank:
            print(' ',end=' ')
        else:
            print(chr(cnt),end=' ')
            cnt+=1
            if cnt==ord('Z')+1:
                cnt=ord('A')
    blank+=1
    print()

n,q=map(int,input().split())
arr=list(map(int,input().split()))

for i in range(q):
    query=input().split()
    
    if query[0]=='print':
        
        if len(query)==2:
            idx=int(query[1])
            print(f'>> {arr[idx-1]}')
        
        else:
            a,b=int(query[1]),int(query[2])
            print('>>',end=' ')

            for j in range(a,b+1):
                print(arr[j-1],end=' ')
            print()
    
    else:
        a=int(query[1])
        
        if a in arr:
            print('>>',arr.index(a)+1)
        
        else:
            print('>>', 0)

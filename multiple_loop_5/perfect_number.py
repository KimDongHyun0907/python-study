inp=input().split()
a,b=int(inp[0]),int(inp[1])

cnt=0
for i in range(a,b+1):
    sum_val=0
    for j in range(1,i):
        if i%j==0:
            sum_val+=j
    if sum_val==i:
        print(f'{i}는 완전수')
        cnt+=1

print(f'완전수 개수는 {cnt}개')

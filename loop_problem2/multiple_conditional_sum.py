inp=input('a,b 입력: ').split()
a,b=int(inp[0]), int(inp[1])

inp2=input('n,m 입력: ').split()
n,m=int(inp2[0]),int(inp2[1])

sum_val=0
for i in range(a,b+1):
    if i%n==0 and i%m!=0:
        sum_val+=i

print(sum_val)

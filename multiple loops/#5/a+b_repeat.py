n=int(input())

for i in range(n):
    inp=input().split()
    a,b=int(inp[0]),int(inp[1])

    sum_val=0
    for j in range(a,b+1):
        sum_val+=j
    print(sum_val)

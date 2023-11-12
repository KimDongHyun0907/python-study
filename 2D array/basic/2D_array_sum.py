n=int(input())

arr2=[list(map(int,input().split())) for _ in range(n)]

sum_val=0
for i in range(n):
    for j in range(n):
        sum_val+=arr2[j][i]
    print(sum_val)
    sum_val=0

a,b=map(int,input().split())

col_avg=[[] for _ in range(a)]
row_avg=[[] for _ in range(b)]
total_avg=0

arr=[list(map(int,input().split())) for _ in range(a)]
for i in range(a):
    for j in range(b):
        col_avg[i].append(arr[i][j])
        row_avg[j].append(arr[i][j])

for i in range(a):
    print(f'{sum(col_avg[i])/b:.2f}',end=' ')
print()
for i in range(b):
    print(f'{sum(row_avg[i])/a:.2f}',end=' ')
print()
for i in range(a):
    total_avg+=sum(arr[i])
print(f'{total_avg/(a*b):.2f}')

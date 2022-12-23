a,b=map(int,input().split())
result=str(a*b)
c=[0 for _ in range(10)]

for i in result:
    c[int(i)]+=1

print(f'두 수의 곱 : {result}')
for i in range(10):
    if c[i]!=0:
        print(f'{i} : {c[i]}')

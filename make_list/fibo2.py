n=int(input())

a,b=1,1
for i in range(3,n+1):
    a,b=b,a+b
print(f'{n}번째 수는 {b}')

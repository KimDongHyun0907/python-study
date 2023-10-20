n=int(input())

prod=1
i=1
while prod<n:
    prod*=i
    if prod>=n:
        break
    i+=1
print(f'1부터 {i}까지의 곱 {prod}')

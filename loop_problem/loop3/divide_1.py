n=int(input())

cnt=0
i=1
while n>1:
    print(f'{n} / {i} = {n//i}')
    n=n//i
    i+=1
    cnt+=1

print(f'{cnt}번 계산')

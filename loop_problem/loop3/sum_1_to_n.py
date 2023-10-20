n=int(input())

sum_val=0
i=1
while sum_val<n:
    sum_val+=i
    if sum_val>=n:
        break
    i+=1
print(f'1부터 {i}까지의 합 {sum_val}')

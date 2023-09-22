inp=input('두 수 입력: ').split()
a,b=int(inp[0]), int(inp[1])
n=int(input('배수 입력: '))

sum_val=0
cnt=0

for i in range(a,b+1):
    if i%n==0:
        sum_val+=i
        cnt+=1
avg=sum_val/cnt

print(f'합계: {sum_val}, 평균: {avg:.2f}')

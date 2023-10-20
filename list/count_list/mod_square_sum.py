a,b=map(int,input().split())
count_arr=[0]*10

while True:
    print(f'{a} / {b} = {a//b} ... {a%b}')
    count_arr[a%b]+=1
    a=a//b
    if a<=1: break

sum_val=0
for i in range(0,10):
    if count_arr[i]!=0:
        print(f'{i}는 {count_arr[i]}번')
    sum_val+=count_arr[i]**2
print(sum_val)

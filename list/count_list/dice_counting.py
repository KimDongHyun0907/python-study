arr=list(map(int,input().split()))

count_arr=[0]*7
for i in arr:
    count_arr[i]+=1

for i in range(1,7):
    print(f'{i}는 {count_arr[i]}번')

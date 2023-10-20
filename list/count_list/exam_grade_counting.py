arr=list(map(int,input().split()))

count_arr=[0]*11
for i in arr:
    count_arr[i//10]+=1

for i in range(10,0,-1):
    print(f'{i*10}-{count_arr[i]}')

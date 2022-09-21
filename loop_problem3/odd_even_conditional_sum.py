sum_val=0
cnt=0

while True:
    n=int(input())
    if n%2==0:
        sum_val+=(n//2)
        cnt+=1
    else:
        sum_val+=n
    if cnt==5: 
        break

print(sum_val)

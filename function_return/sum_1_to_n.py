def sum1toN(n):
    sum_val=0
    for i in range(1,n+1):
        sum_val+=i
    return sum_val

n=int(input())
print(sum1toN(n))

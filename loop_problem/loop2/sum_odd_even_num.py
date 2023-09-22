n=int(input())

sum_odd, sum_even=0,0
for _ in range(n):
    m=int(input())
    if m%2==0:
        sum_even+=m
    else:
        sum_odd+=m

print(sum_odd,sum_even)

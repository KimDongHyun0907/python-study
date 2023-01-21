def total_sum(n):
    if n==1: return 1
    return total_sum(n-1)+n

n=int(input())
print(total_sum(n))

def odd_or_even_sum(n):
    if n==1: return 1
    if n==2: return 2
    
    return odd_or_even_sum(n-2)+n

n=int(input())
print(odd_or_even_sum(n))

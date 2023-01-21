def get_count(n):
    if n==1: return 0
    
    if n%2==0: return get_count(n//2)+1
    else: return get_count(n//3)+1

n=int(input())
print(get_count(n))

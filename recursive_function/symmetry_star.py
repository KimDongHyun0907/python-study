def print_star(n):
    if n==0: return
    print('* '*n)
    print_star(n-1)
    if n==1: return
    print('* '*n)

n=int(input())
print_star(n)

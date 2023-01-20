def print_number_sort(n,m):
    if n==0: return
    if n==1 and m==1: return
    print_number_sort(n-1,m)
    print(n,end=' ')

def print_number_reverse(n):
    if n==0: return
    print(n,end=' ')
    print_number_reverse(n-1)

def order_print(n):
    print_number_sort(n,0)
    print_number_reverse(n-1)
    print()
    print_number_reverse(n)
    print_number_sort(n,1)

n=int(input())
order_print(n)

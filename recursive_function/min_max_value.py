def max_value(n):
    if n==1: return arr[n-1]
    return max(max_value(n-1),arr[n-1])

def min_value(n):
    if n==1: return arr[n-1]
    return min(min_value(n-1),arr[n-1])

n=int(input())
arr=list(map(int,input().split()))
print(max_value(n))
print(min_value(n))

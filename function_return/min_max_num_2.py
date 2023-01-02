def min_number(*args):
    return min(args)

def max_number(*args):
    return max(args)

a,b,c=map(int,input().split())
print(min_number(a,b,c))
print(max_number(a,b,c))

n,m=map(int,input().split())

def two_num_gcd(n,m):
    min_num=min(n,m)
    for i in range(min_num,0,-1):
        if n%i==0 and m%i==0:
            print(i)
            break

two_num_gcd(n,m)

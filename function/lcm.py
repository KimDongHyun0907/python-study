n,m=map(int,input().split())

def two_num_lcm(n,m):
    max_num=max(n,m)
    for i in range(max_num,n*m+1,max_num):
        if i%n==0 and i%m==0:
            print(i)
            break

two_num_lcm(n,m)

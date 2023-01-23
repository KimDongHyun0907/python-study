def lcm(a,b):
    for i in range(1,a+1):
        if b*i%a==0: return b*i 

def lcm_arr(n):
    if n==1:
        return arr[n-1]
    return lcm(lcm_arr(n-1),arr[n-1])

n=int(input())
arr=list(map(int,input().split()))
print(lcm_arr(n))

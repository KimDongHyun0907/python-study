def plus_minus_change(arr):
    for elem in range(n):
        arr[elem]=arr[elem]*(-1)

n=int(input())
num_list=list(map(int,input().split()))
plus_minus_change(num_list)
print(sum(num_list))

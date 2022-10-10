arr=list(map(int,input().split()))
arr=arr[2::3]
print(arr)
print(f'{sum(arr)/len(arr):.2f}')

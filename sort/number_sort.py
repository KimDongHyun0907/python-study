arr=[15,64,32,78,36,98,22]
arr.sort()
print(arr) # [15, 22, 32, 36, 64, 78, 98]

arr=[15,64,32,78,36,98,22]
arr.sort(reverse=True)
print(arr) # [98, 78, 64, 36, 32, 22, 15]

arr=[15,64,32,78,36,98,22]
sort_arr=sorted(arr)
print(sort_arr) # [15, 22, 32, 36, 64, 78, 98]

arr=[15,64,32,78,36,98,22]
sort_arr=sorted(arr,reverse=True)
print(sort_arr) # [98, 78, 64, 36, 32, 22, 15]

arr=[15,64,32,78,36,98,22]
arr.sort()
sort_arr=arr[::-1]
print(sort_arr) # [98, 78, 64, 36, 32, 22, 15]

arr=[15,64,32,78,36,98,22]
arr.sort()
sort_arr=list(reversed(arr))
print(sort_arr) # [98, 78, 64, 36, 32, 22, 15]

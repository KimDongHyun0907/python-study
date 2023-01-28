n,k,string=input().split()
n,k=int(n),int(k)
arr=[]

for _ in range(n):
    input_string=input()
    if len(string)<=len(input_string):
        if input_string[0:len(string)]==string: arr.append(input_string)

arr.sort()
print(arr[k-1])

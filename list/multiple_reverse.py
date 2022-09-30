n=int(input())

arr=list(map(int,input().split()))

n_mul=[]
for i in arr:
    if i%n==0:
        n_mul.append(i)

for i in n_mul[::-1]:
    print(i,end=' ')

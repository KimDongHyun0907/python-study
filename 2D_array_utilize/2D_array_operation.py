n=int(input())
arr1=[list(map(int,input().split())) for _ in range(n)]
input()
arr2=[list(map(int,input().split())) for _ in range(n)]

print('1. 덧셈 \n2. 뺄셈 \n3. 곱셈 \n4. 나눗셈')
num=int(input('번호를 선택.'))

arr3=[[0 for _ in range(n)] for _ in range(n)]

if num==1:
    for i in range(n):
        for j in range(n):
            arr3[i][j]=arr1[i][j]+arr2[i][j]

elif num==2:
    for i in range(n):
        for j in range(n):
            arr3[i][j]=arr1[i][j]-arr2[i][j]

elif num==3:
    for i in range(n):
        for j in range(n):
            arr3[i][j]=arr1[i][j]*arr2[i][j]

elif num==4:
    for i in range(n):
        for j in range(n):
            arr3[i][j]=arr1[i][j]//arr2[i][j]

for i in arr3:
    for j in i:
        print(j,end=' ')
    print()

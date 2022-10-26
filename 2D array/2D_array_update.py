n=int(input())

arr2=[list(map(int,input().split())) for _ in range(n)]
print(arr2[1][2])  # 2행 3열

arr2[1][2]=100
print(arr2)

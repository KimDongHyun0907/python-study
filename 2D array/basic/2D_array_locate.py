n=int(input())

arr2=[list(map(int,input().split())) for _ in range(n)]
print(arr2[1][2])  # 2행 3열
print(arr2[0][3])  # 1행 4열

a,b=map(int,input().split())

arr=[input().split() for _ in range(a)]
for i in range(a):
    for j in range(b):
        # 소문자 -> 대문자
        if ord(arr[i][j])>= ord('a') and ord(arr[i][j])<=ord('z'):
            arr[i][j]=chr(ord(arr[i][j])-32)
        
        # 대문자 -> 소문자
        elif ord(arr[i][j])>= ord('A') and ord(arr[i][j])<=ord('Z'):
            arr[i][j]=chr(ord(arr[i][j])+32)

for i in range(a):
    for j in range(b):
        print(arr[i][j],end=' ')
    print()

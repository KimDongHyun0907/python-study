n=int(input())

for i in range(n):
    # 공백
    for j in range(n-1-i):
        print(' ',end='')
    
    # 별
    for j in range(2*i+1):
        print('*',end='')
    
    print()

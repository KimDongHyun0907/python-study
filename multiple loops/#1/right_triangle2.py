n=int(input())

for i in range(n):
    for j in range(i+1):
        for k in range(i+1):
            print('*',end='')
        print(end=' ')
    print()

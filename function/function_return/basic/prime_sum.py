def isPrimeList(a,b):
    primenum=[]
    for i in range(a,b+1):
        if i==1: continue
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
                break
        if isPrime:
            primenum.append(i)
    return primenum

def PrintPrimeNum(a,b,prime_list):
    print(f'{a}와 {b} 사이의 소수들은',end=' ')
    for i in prime_list:
        print(f'{i} ',end='')
    print()

def PrimeSum(a,b,prime_list):
    sum_val=0
    for i in prime_list:
        sum_val+=i
    print(f'{a}와 {b} 사이에 있는 소수들의 합은 {sum_val}입니다.')

a,b=map(int,input().split())
prime_list=isPrimeList(a,b)
PrintPrimeNum(a,b,prime_list)
PrimeSum(a,b,prime_list)

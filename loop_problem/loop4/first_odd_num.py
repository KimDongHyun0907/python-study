while True:
    n=int(input())
    if n%2!=0:
        print('짝수를 입력')
        continue
    else:
        break

cnt=1
while True:
    if n%2==0:
        print(f'{cnt}. {n} : 짝수')
        n=n//2
        cnt+=1
    else:
        print(f'{cnt}. {n} : 홀수')
        break

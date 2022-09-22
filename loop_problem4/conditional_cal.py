n=int(input())
cnt=1

while True:
    if n%2==0:
        print(f'{cnt}. {n} * 3 + 1 = {n*3+1}')
        n=n*3+1
    else:
        print(f'{cnt}. {n} * 2 + 2 = {n*2+2}')
        n=n*2+2
    
    cnt+=1
    
    if n>=1000:
        break

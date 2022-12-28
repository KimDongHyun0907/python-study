n=int(input())

def make_num_square(n):
    cnt=1
    isIncorDec=True  

    for _ in range(n):
        for _ in range(n):
            print(cnt,end=' ')
            if cnt==9: isIncorDec=False
            elif cnt==1: isIncorDec=True
            
            if isIncorDec==True: cnt+=1
            else: cnt-=1
        print()

make_num_square(n)

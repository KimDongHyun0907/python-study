n=int(input())

a,b,c=0,0,0
for i in range(n):
    if i%5==0:
        c+=1
    elif i%3==0:
        b+=1
    elif i%2==0:
        a+=1

print(f'A:{a}, B:{b}, C:{c}')

inp=input().split()
h,w=int(inp[0]),int(inp[1])

bmi=w//((h*0.01)**2)
print(bmi)

if bmi>=25:
    print('obesity')

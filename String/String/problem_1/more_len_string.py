a,b=input().split()

if len(a)<len(b):
    print(b,len(b)-len(a))
elif len(a)==len(b):
    print('same')
else:
    print(a,len(a)-len(b))

s=input()
q=input()

for i in q:
    if i=='L':
        s=s[1:]+s[0]
        print(f'L : {s}')
    elif i=='R':
        s=s[-1]+s[:-1]
        print(f'R : {s}')
print(s)

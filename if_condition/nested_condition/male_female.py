inp=input().split()
gender, age=inp[0], int(inp[1])

if gender=='M':
    if age>=19: print('Man')
    else: print('Boy')
else:
    if age>=19: print('Woman')
    else: print('Girl')

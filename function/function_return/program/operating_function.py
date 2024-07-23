def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiple(a,b):
    return a*b

def divide(a,b):
    return a//b

def modular(a,b):
    return a%b

def square(a,b):
    return a**b

def operator(a,o,b):
    if o=='+':
        return plus(a,b)
    if o=='-':
        return minus(a,b)
    if o=='*':
        return multiple(a,b)
    if o=='/':
        return divide(a,b)
    if o=='%':
        return modular(a,b)
    if o=='^':
        return square(a,b)
    else:
        return False


inp=input().split()
inp[0],inp[2]=int(inp[0]),int(inp[2])
print(operator(inp[0],inp[1],inp[2]))

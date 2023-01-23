def function(n):
    if n==1:
        return 0
    if n%2==0:
        return function(n//2)+1
    else:
        return function(3*n+1)+1

print(function(int(input())))

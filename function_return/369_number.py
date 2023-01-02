def is_369_number(n):
    while n>0:
        if n%10==3 or n%10==6 or n%10==9: return True
        n//=10
    return False

n=int(input())

if is_369_number(n): print('Yes')
else: print('No')

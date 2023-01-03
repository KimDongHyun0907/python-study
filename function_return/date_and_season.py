def leapyear(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def range_day(a,b):
    if d>=a and d<=b: return True
    else: return False

def YesOrNo(y,m,d):
    if m==2:
        if leapyear(y): return range_day(1,29)
        else: return range_day(1,28)
    elif m in [4,6,9,11]:
        return range_day(1,30)
    elif m in [1,3,5,7,8,10,12]:
        return range_day(1,31)
    else:
        return False

def season(m):
    if m in [3,4,5]:
        return '봄'
    elif m in [6,7,8]:
        return '여름'
    elif m in [9,10,11]:
        return '가을'
    else:
        return '겨울'

y,m,d=map(int,input().split())

if YesOrNo(y,m,d): 
    print('Yes')
    print(f'계절은 {season(m)}')
else: 
    print('No')
    print('계절은 None')

def isLeapYear(y):
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

def MakeLeapYearList(y1,y2):
    LeapYearList=[]
    print(f'{y1}과 {y2} 사이의 윤년은 ',end='')
    for year in range(y1,y2+1):
        if isLeapYear(year):
            print(f'{year} ',end='')
            LeapYearList.append(year)
    print()
    return LeapYearList

def CountLeapYear(LeapYearList):
    print(f'{y1}과 {y2} 사이의 윤년은 총 {len(LeapYearList)}개 이다.')

y1,y2=map(int,input().split())
LeapYearList=MakeLeapYearList(y1,y2)
CountLeapYear(LeapYearList)

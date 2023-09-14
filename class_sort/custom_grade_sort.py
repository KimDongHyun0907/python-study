from functools import cmp_to_key

n=int(input())
student_points=[tuple(map(int,input().split())) for _ in range(n)]

def compare_two_points(x,y,a,b):
    if x[a]+x[b]<y[a]+y[b]:
        return 1
    elif x[a]+x[b]>y[a]+y[b]:
        return -1
    else:
        return 0

def compare(x,y):
    if (x[0]+x[1])%3==0 and (y[0]+y[1])%3!=0:
        return -1
    elif (y[0]+y[1])%3==0 and (x[0]+x[1])%3!=0:
        return 1
    else:
        if (x[0]+x[1])%3==0 and (y[0]+y[1])%3==0:
            return compare_two_points(x,y,0,1)
        elif (x[0]+x[1])%3!=0 and (y[0]+y[1])%3!=0:
            return compare_two_points(x,y,1,2)

student_points.sort(key=cmp_to_key(compare))

for kor,math,eng in student_points:
    print(kor,math,eng)

class Student:
    def __init__(self, kor, math, eng):
        self.kor=kor
        self.math=math
        self.eng=eng
    
student_points=[]
n=int(input())
for _ in range(n):
    kor,math,eng=map(int,input().split())
    student_points.append(Student(kor,math,eng))

student_points.sort(key=lambda x:-(x.kor+x.math+x.eng))
for point in student_points:
    print(point.kor, point.math, point.eng, point.kor+point.math+point.eng)

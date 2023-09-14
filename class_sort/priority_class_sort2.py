class Student:
    def __init__(self, kor, math, eng):
        self.kor = kor
        self.math = math
        self.eng = eng

n=int(input())
student_point=[]
for _ in range(n):
    kor,math,eng=tuple(map(int,input().split()))
    student_point.append(Student(kor,math,eng))

student_point.sort(key=lambda x:(x.math, -x.kor))
for point in student_point:
    print(point.kor, point.math, point.eng)

class Student:
    def __init__(self,kor=0,math=0,eng=0):
        self.kor=kor
        self.math=math
        self.eng=eng

students=[]
for _ in range(3):
    kor,math,eng=map(int,input().split())
    students.append(Student(kor,math,eng))

print(students[1].kor,students[1].math,students[1].eng) # 2번째 학생 점수

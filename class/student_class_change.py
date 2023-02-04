class Student:
    def __init__(self,kor=0,math=0,eng=0):
        self.grade1=kor
        self.grade2=math
        self.grade3=eng

student=Student()
print(student.grade1)
print(student.grade2)
print(student.grade3)

student.grade1=70
student.grade2=80
student.grade3=90

print(student.grade1)
print(student.grade2)
print(student.grade3)

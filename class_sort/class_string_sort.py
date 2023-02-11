class Student:
    def __init__(self,kor,math,eng,name):
        self.kor=kor
        self.math=math
        self.eng=eng
        self.name=name

input_data=[tuple(input().split()) for _ in range(5)]
students=[Student(int(kor),int(math),int(eng),name) for kor, math, eng, name in input_data]

print()
students.sort(key=lambda x: x.name)
for student in students:
    print(student.kor, student.math, student.eng,student.name)

print()
students.sort(key=lambda x: x.name,reverse=True)
for student in students:
    print(student.kor, student.math, student.eng,student.name)

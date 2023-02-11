class Student:
    def __init__(self,kor,math,eng):
        self.kor=kor
        self.math=math
        self.eng=eng

input_data=[tuple(input().split()) for _ in range(5)]
students=[Student(int(kor),int(math),int(eng)) for kor, math, eng in input_data]
print()
for student in students:
    print(student.kor,student.math,student.eng)
print()

#students.sort(key=lambda x:x.kor) # 국어 오름차순
students.sort(key=lambda x: -x.math) # 수학 내림차순
for student in students:
    print(student.kor,student.math,student.eng)

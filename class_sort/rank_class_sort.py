class Student:
    def __init__(self, kor, math, eng, num):
        self.kor = kor
        self.math = math
        self.eng = eng
        self.num = num


n = int(input())
student_points = []
for num in range(1, n+1):
    kor, math, eng = map(int, input().split())
    student_points.append(Student(kor, math, eng, num))

student_points.sort(key=lambda x: -(x.kor+x.math+x.eng))

for idx, student in enumerate(student_points, start=1):
    print(f'{idx}등은 총점 {student.kor+student.math+student.eng}인 {student.num}번 학생입니다.')

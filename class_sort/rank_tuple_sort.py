n = int(input())
student_points = [tuple(map(int, input().split())) for _ in range(n)]
student_points = list(enumerate(student_points, start=1))
# student_points = [(1, (60, 80, 40)), (2, (30, 70, 90)), (3, (80, 10, 30)), (4, (40, 70, 60)), (5, (50, 10, 70))]

student_points.sort(key=lambda x: -(x[1][0]+x[1][1]+x[1][2]))
# student_points = [(1, (2, (30, 70, 90))), (2, (1, (60, 80, 40))), (3, (4, (40, 70, 60))), (4, (5, (50, 10, 70))), (5, (3, (80, 10, 30)))]
for idx, (num, (kor, math, eng)) in enumerate(student_points, start=1):
    print(f'{idx}등은 총점이 {kor+math+eng}점인 {num}번 학생입니다.')

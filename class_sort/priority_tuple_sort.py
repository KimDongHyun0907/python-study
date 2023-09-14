n=int(input())
student_points=[tuple(map(int,input().split())) for _ in range(n)]

student_points.sort(key=lambda x: (-x[2],-x[0], -x[1]))
for kor, math, eng in student_points:
    print(kor, math, eng)

"""
날짜 변경 후 출력
입력 : yyyy.mm.dd
출력 : mm-dd-yyyy
"""
day=input()
day=day.split('.')
print(f'{day[1]}-{day[2]}-{day[0]}')
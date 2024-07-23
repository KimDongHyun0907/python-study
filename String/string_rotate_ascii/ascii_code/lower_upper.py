x='H'
print(ord(x))  # 72
print(ord(x)-ord('A'))  # 7
print(ord(x)-ord('A')+ord('a'))  # x의 소문자 아스키 번호 = 104
print(chr(ord(x)-ord('A')+ord('a')))  # 아스키 번호를 문자로 변환 h

-----------------------------------------------------------------------

x=input()

print(chr(ord(x)-ord('a')+ord('A')))

-----------------------------------------------------------------------

print('A'.lower())
print('a'.upper())

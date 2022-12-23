n=int(input())
result=0
for _ in range(n):
    num=int(input())
    result+=num

m=int(input())
result=str(result)
cnt=m%len(result)
new_result=result[cnt:]+result[0:cnt]
print(f'{result}를 {m}번 회전 : {new_result}')

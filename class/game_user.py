class User:
    def __init__(self,id="GameManager",level=100):
        self.id=id
        self.level=level

n=int(input())
users=[User()]
for _ in range(n):
    id,level=input().split()
    level=int(level)
    users.append(User(id,level))

max_level_idx=0
name_idx=0

for i in range(n+1):
    print(f'id : {users[i].id}, level : {users[i].level}')
    if users[i].level>users[max_level_idx].level:
        max_level_idx=i
    
    if users[i].id>users[name_idx].id:
        name_idx=i


print(f'가장 높은 레벨의 아이디는 {users[max_level_idx].id}')
print(f'사전순으로 가장 나중에 오는 아이디는 {users[name_idx].id} 레벨은 {users[name_idx].level}')

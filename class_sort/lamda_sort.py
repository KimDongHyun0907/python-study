# even_number first
a=[1,2,3,4,5,6,7,8,9]
a.sort(key=lambda x:x%2)
print(a)

# reverse sort
a=[1,2,3,4,5,6,7,8,9]
a.sort(key=lambda x:-x)
print(a)

# odd_number first
a=[1,2,3,4,5,6,7,8,9]
a.sort(key=lambda x:x%2==0)
print(a)

arr=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
for i in range(3):
    for j in range(4):
        print(arr[i][j],end=' ')
    print()
    
arr=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
for i in arr:
    for j in i:
        print(j,end=' ')
    print()

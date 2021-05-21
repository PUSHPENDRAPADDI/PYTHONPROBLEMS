arr = [[1,2,3],[4,5,6],[7,8,9]]
pro = 1
for i in range(len(arr)):
    for j in range(len(arr)):
        pro= pro *arr[i][j]
print(pro)   
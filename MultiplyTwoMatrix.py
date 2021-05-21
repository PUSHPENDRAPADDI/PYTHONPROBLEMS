arr = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
arr2 = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
rev = [[1,2,3,4],[4,5,6,5],[7,8,9,5],[4,5,7,8]]
for i in range(len(arr)):
    for j in range(len(arr)):
        rev[i][j] = 0
        for k in range(len(arr)):
            rev[i][j] += arr[i][k]*arr2[k][j]  
        print(rev[i][j], end = " ") 
    print("")    
arr =  [["Sunny", "hum", "Paddi"],["Achhaa","dost", "Bimaar"]]
res = [1,2,3,4,5,6]
for i in range(len(arr)-1):
    for j in range(len(arr)):
        res[i] = arr[i][j] + arr[i+1][j]
        print(res[i], end = " ")
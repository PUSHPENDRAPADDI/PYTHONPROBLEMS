row = int(input("Enter the length of row for matrix "))
cal = int(input("Enter the length of calumn for matrix "))
arr =  [[1,2,4,5,6,7,3],[4,5,5,5,5,5,6],[7,8,3,4,3,3,9],[7,8,3,4,3,3,9]]
for i in range(row):
    for j in range(cal):
        arr[i][j] = int(input("Enter element of matrics = "))
for i in range(row):
    for j in range(cal):
        print(arr[i][j], end = " ")
    print(" ")
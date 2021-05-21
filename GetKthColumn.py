arr =  [[1,2,4,5,6,7,3],[4,5,5,5,5,5,6],[7,8,3,4,3,3,9],[7,8,3,4,3,3,9]]
row = int(input("Enter row = "))
for i in range(4):
    if i== row:
        for j in range(7):
            print(arr[i][j], end = " ")
        print(" ")
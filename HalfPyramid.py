num=int(input("Enter number for pattern = "))
for i in range(0,num+1):
    for j in range(0,num+1):
        if j>num-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
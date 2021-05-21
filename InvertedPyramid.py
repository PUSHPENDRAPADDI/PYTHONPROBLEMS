num = int(input("Enter the number to print the pattern = "))
for i in range(0,num):
    for j in range(0, 2*num-i):
        if j >= i:
            print("*",end=' ')
        else:
            print(" ",end=' ') 
    print('') 
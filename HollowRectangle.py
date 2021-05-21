num = int(input("Enter the number to print the pattern = "))
for i in range(0,num):
    for j in range(0, num+3):
        if j == num+2 or j==0 or i== 0 or i==num-1:
            print("*",end=' ')
        else:
            print(" ",end=' ') 
    print('') 
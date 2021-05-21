num = int(input("Enter the number to print the pattern = "))
for i in range(0,num):
    for j in range(0, 2*num-i):
        if j == i or j==2*num-i-1 or i== 0:
            print(j,end=' ')
        else:
            print(" ",end=' ') 
    print('') 
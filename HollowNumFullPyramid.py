num = int(input("Enter the number to print the pattern = "))
for i in range(0,num):
    for j in range(0, num+i):
        if j == num-(i+1) or j == num+i-1 or i == num-1:
            print(j,end=' ')
        else:
            print(" ",end=' ') 
    print('') 